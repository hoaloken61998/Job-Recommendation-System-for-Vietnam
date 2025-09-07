# =======================================================================
#  Job Recommender App for Local Development
# =======================================================================
#
#  Instructions to run locally:
#  1. Save this code as a Python file (e.g., app.py).
#  2. Make sure your data files ('processed_candidate.csv', 'df_job_processed.csv', 'expanded_df.csv')
#     are in the SAME FOLDER as this script.
#  3. Open a terminal or command prompt in that folder.
#  4. Install the required libraries by running:
#     pip install streamlit pandas scikit-learn
#  5. Run the app with the command:
#     streamlit run app.py
#
# =======================================================================

import streamlit as st
import pandas as pd
import traceback

def show_candidate_profile(candidate_id, candidate_df):
    """
    Helper function to display the profile of a selected candidate with a defined layout and Vietnamese labels.
    """
    st.header("👤 Hồ sơ ứng viên")
    candidate_info = candidate_df[candidate_df['candidate_id'] == candidate_id]

    if candidate_info.empty:
        st.warning("Không tìm thấy ứng viên với ID này.")
        return

    # Extract the first row of data
    candidate = candidate_info.iloc[0]

    # Define which columns to display and their Vietnamese labels
    profile_map = {
        'user_name': 'Tên ứng viên',
        'desired_job_translated': 'Công việc mong muốn',
        'industry': 'Ngành nghề',
        'workplace_desired': 'Nơi làm việc mong muốn'
    }

    # Create a two-column layout for the profile
    col1, col2 = st.columns(2)
    
    with col1:
        # Display Name and Desired Job
        st.subheader(profile_map['user_name'])
        st.write(candidate.get('user_name', 'N/A'))
        
        st.subheader(profile_map['desired_job_translated'])
        st.write(candidate.get('desired_job_translated', 'N/A'))

    with col2:
        # Display Industry and Workplace
        st.subheader(profile_map['industry'])
        st.write(candidate.get('industry', 'N/A'))

        st.subheader(profile_map['workplace_desired'])
        st.write(candidate.get('workplace_desired', 'N/A'))


def display_recommendations(candidate_id, job_df, expanded_df):
    """
    Helper function to display recommendations with Vietnamese labels and a clickable URL.
    """
    st.header("📊 Các công việc được đề xuất")

    # Filter expanded_df for the selected candidate
    recommendations = expanded_df[expanded_df['candidate_id'] == candidate_id]

    if not recommendations.empty:
        # Sort by hybrid_score to get the best recommendations first
        recommendations = recommendations.sort_values(by='hybrid_score', ascending=False)
        # Get the recommended job IDs (which are the indices of the Job df)
        recommended_job_ids = recommendations['expanded_job_id'].tolist()

        # Retrieve job details from the job_df using the indices
        recommended_jobs = job_df.iloc[recommended_job_ids]

        if not recommended_jobs.empty:
            st.write(f"Tìm thấy {len(recommended_jobs)} công việc được đề xuất.")
            
            # Define which columns to display and their Vietnamese labels
            display_cols = {
                'Job_Name': 'Tên công việc',
                'Company_name': 'Tên công ty',
                'Location': 'Địa điểm',
                'Salary': 'Mức lương',
                'URL': 'Đường dẫn'
            }
            
            # Filter for columns that actually exist in the dataframe to avoid errors
            existing_cols = [col for col in display_cols.keys() if col in recommended_jobs.columns]
            
            # Create a new dataframe with only the columns we need
            display_df = recommended_jobs[existing_cols].rename(columns=display_cols)
            
            # Use st.column_config to make the URL column clickable
            st.dataframe(
                display_df,
                column_config={
                    "Đường dẫn": st.column_config.LinkColumn(
                        "Link",
                        display_text="Mở trang tuyển dụng"
                    )
                },
                hide_index=True,
                use_container_width=True
            )
        else:
            st.warning("Không thể tìm thấy thông tin chi tiết cho các công việc được đề xuất.")
    else:
        st.warning(f"Không tìm thấy đề xuất nào cho ứng viên có ID: {candidate_id}")


def main():
    """
    Main function to run the Streamlit job recommendation app.
    """
    st.set_page_config(layout="wide", page_title="Hệ thống đề xuất việc làm")

    try:
        st.title("👨‍💼 Hệ thống đề xuất việc làm 👩‍💼")

        # --- Data Loading (Internal) ---
        CANDIDATE_PATH = 'processed_candidate.csv'
        JOB_PATH = 'df_job_processed.csv'
        EXPANDED_PATH = 'expanded_df.csv'

        @st.cache_data
        def load_data(candidate_path, job_path, expanded_path):
            # Load the datasets
            candidate_df = pd.read_csv(candidate_path)
            job_df = pd.read_csv(job_path)
            expanded_df = pd.read_csv(expanded_path)

            # Create 'candidate_id' from the dataframe index
            candidate_df = candidate_df.reset_index().rename(columns={'index': 'candidate_id'})
            
            return candidate_df, job_df, expanded_df

        candidate_df, job_df, expanded_df = load_data(CANDIDATE_PATH, JOB_PATH, EXPANDED_PATH)

        if candidate_df is not None:
            st.sidebar.header("Tìm kiếm ứng viên")
            
            # Input field for candidate_id
            with st.sidebar.form("candidate_search_form"):
                candidate_id_input = st.number_input(
                    label="Nhập ID ứng viên:",
                    min_value=0,
                    step=1
                )
                submit_button = st.form_submit_button(label="Tìm kiếm")

            if submit_button:
                # Show the selected candidate's information
                show_candidate_profile(candidate_id_input, candidate_df)
                
                st.divider() # Visual separator

                # Display the recommendations for that candidate
                display_recommendations(candidate_id_input, job_df, expanded_df)
    
    except FileNotFoundError as e:
        st.error(f"Lỗi: Không tìm thấy tệp dữ liệu.")
        st.error(f"Chi tiết: {e}")
        st.info("Vui lòng đảm bảo các tệp sau nằm trong cùng một thư mục với tập lệnh:")
        st.info(f"- {CANDIDATE_PATH}\n- {JOB_PATH}\n- {EXPANDED_PATH}")
    
    except Exception as e:
        st.error("Đã xảy ra lỗi không mong muốn trong ứng dụng.")
        st.error(f"Chi tiết lỗi: {e}")
        traceback.print_exc()


if __name__ == "__main__":
    main()
