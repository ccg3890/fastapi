from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

tags_metadata = [
    {
        "name": "category",
        "description": "검색조건에서 사용하고 있는 카테고리 리스트",
    },
    {
        "name": "company",
        "description": "검색조건에서 사용하고 있는 회사 리스트",
    },
    {
        "name": "summary",
        "description": "검색 후 사용되는 카드 리스트",
    },
    {
        "name": "101",
        "description": "chart data 예제 101",
    },
    {
        "name": "102",
        "description": "chart data 예제 102",
    },
]


app = FastAPI(openapi_tags=tags_metadata)

@app.get("/category/list",tags=["category"])
async def category_list():
    return {
        "result": {
            "code": "200",
            "data": [
                {
                    "product_id": '',
                    "creator_user_id": '',
                    "modified_user_id": '',
                    "user_id": '',
                    "contents_id": '',
                    "seq_id": '',
                    "status": "active",
                    "created_date": '',
                    "modified_date": '',
                    "search_type": '',
                    "search_keyword": '',
                    "company_name": '',
                    "type": '',
                    "start_date": '',
                    "end_date": '',
                    "title": '',
                    "hits": '',
                    "price_type": '',
                    "email": '',
                    "level_cd": '',
                    "gen": '',
                    "sns_code": '',
                    "ref_tel": '',
                    "company_tel": '',
                    "phone_number": '',
                    "tel": '',
                    "corp_ids": '',
                    "status_arr": '',
                    "data_type_arr": '',
                    "category_arr": '',
                    "not_corp_ids": '',
                    "page_num": '',
                    "page_size": '',
                    "total_size": '',
                    "category_id": "CA000001",
                    "category_name": "경제/산업",
                    "parent_id": '',
                    "grade": "1",
                    "corp_id": '',
                    "category_ids": '',
                    "category_nms": '',
                    "grades": ''
                },
                {
                    "product_id": '',
                    "creator_user_id": '',
                    "modified_user_id": '',
                    "user_id": '',
                    "contents_id": '',
                    "seq_id": '',
                    "status": "active",
                    "created_date": '',
                    "modified_date": '',
                    "search_type": '',
                    "search_keyword": '',
                    "company_name": '',
                    "type": '',
                    "start_date": '',
                    "end_date": '',
                    "title": '',
                    "hits": '',
                    "price_type": '',
                    "email": '',
                    "level_cd": '',
                    "gen": '',
                    "sns_code": '',
                    "ref_tel": '',
                    "company_tel": '',
                    "phone_number": '',
                    "tel": '',
                    "corp_ids": '',
                    "status_arr": '',
                    "data_type_arr": '',
                    "category_arr": '',
                    "not_corp_ids": '',
                    "page_num": '',
                    "page_size": '',
                    "total_size": '',
                    "category_id": "CA000002",
                    "category_name": "금융/증권",
                    "parent_id": '',
                    "grade": "2",
                    "corp_id": '',
                    "category_ids": '',
                    "category_nms": '',
                    "grades": ''
                },
                {
                    "product_id": '',
                    "creator_user_id": '',
                    "modified_user_id": '',
                    "user_id": '',
                    "contents_id": '',
                    "seq_id": '',
                    "status": "active",
                    "created_date": '',
                    "modified_date": '',
                    "search_type": '',
                    "search_keyword": '',
                    "company_name": '',
                    "type": '',
                    "start_date": '',
                    "end_date": '',
                    "title": '',
                    "hits": '',
                    "price_type": '',
                    "email": '',
                    "level_cd": '',
                    "gen": '',
                    "sns_code": '',
                    "ref_tel": '',
                    "company_tel": '',
                    "phone_number": '',
                    "tel": '',
                    "corp_ids": '',
                    "status_arr": '',
                    "data_type_arr": '',
                    "category_arr": '',
                    "not_corp_ids": '',
                    "page_num": '',
                    "page_size": '',
                    "total_size": '',
                    "category_id": "CA000003",
                    "category_name": "통신/인구",
                    "parent_id": '',
                    "grade": "3",
                    "corp_id": '',
                    "category_ids": '',
                    "category_nms": '',
                    "grades": ''
                },
                {
                    "product_id": '',
                    "creator_user_id": '',
                    "modified_user_id": '',
                    "user_id": '',
                    "contents_id": '',
                    "seq_id": '',
                    "status": "active",
                    "created_date": '',
                    "modified_date": '',
                    "search_type": '',
                    "search_keyword": '',
                    "company_name": '',
                    "type": '',
                    "start_date": '',
                    "end_date": '',
                    "title": '',
                    "hits": '',
                    "price_type": '',
                    "email": '',
                    "level_cd": '',
                    "gen": '',
                    "sns_code": '',
                    "ref_tel": '',
                    "company_tel": '',
                    "phone_number": '',
                    "tel": '',
                    "corp_ids": '',
                    "status_arr": '',
                    "data_type_arr": '',
                    "category_arr": '',
                    "not_corp_ids": '',
                    "page_num": '',
                    "page_size": '',
                    "total_size": '',
                    "category_id": "CA000004",
                    "category_name": "소비/상권",
                    "parent_id": '',
                    "grade": "4",
                    "corp_id": '',
                    "category_ids": '',
                    "category_nms": '',
                    "grades": ''
                },
                {
                    "product_id": '',
                    "creator_user_id": '',
                    "modified_user_id": '',
                    "user_id": '',
                    "contents_id": '',
                    "seq_id": '',
                    "status": "active",
                    "created_date": '',
                    "modified_date": '',
                    "search_type": '',
                    "search_keyword": '',
                    "company_name": '',
                    "type": '',
                    "start_date": '',
                    "end_date": '',
                    "title": '',
                    "hits": '',
                    "price_type": '',
                    "email": '',
                    "level_cd": '',
                    "gen": '',
                    "sns_code": '',
                    "ref_tel": '',
                    "company_tel": '',
                    "phone_number": '',
                    "tel": '',
                    "corp_ids": '',
                    "status_arr": '',
                    "data_type_arr": '',
                    "category_arr": '',
                    "not_corp_ids": '',
                    "page_num": '',
                    "page_size": '',
                    "total_size": '',
                    "category_id": "CA000005",
                    "category_name": "이커머스",
                    "parent_id": '',
                    "grade": "5",
                    "corp_id": '',
                    "category_ids": '',
                    "category_nms": '',
                    "grades": ''
                },
                {
                    "product_id": '',
                    "creator_user_id": '',
                    "modified_user_id": '',
                    "user_id": '',
                    "contents_id": '',
                    "seq_id": '',
                    "status": "active",
                    "created_date": '',
                    "modified_date": '',
                    "search_type": '',
                    "search_keyword": '',
                    "company_name": '',
                    "type": '',
                    "start_date": '',
                    "end_date": '',
                    "title": '',
                    "hits": '',
                    "price_type": '',
                    "email": '',
                    "level_cd": '',
                    "gen": '',
                    "sns_code": '',
                    "ref_tel": '',
                    "company_tel": '',
                    "phone_number": '',
                    "tel": '',
                    "corp_ids": '',
                    "status_arr": '',
                    "data_type_arr": '',
                    "category_arr": '',
                    "not_corp_ids": '',
                    "page_num": '',
                    "page_size": '',
                    "total_size": '',
                    "category_id": "CA000006",
                    "category_name": "유통/마케팅",
                    "parent_id": '',
                    "grade": "6",
                    "corp_id": '',
                    "category_ids": '',
                    "category_nms": '',
                    "grades": ''
                },
                {
                    "product_id": '',
                    "creator_user_id": '',
                    "modified_user_id": '',
                    "user_id": '',
                    "contents_id": '',
                    "seq_id": '',
                    "status": "active",
                    "created_date": '',
                    "modified_date": '',
                    "search_type": '',
                    "search_keyword": '',
                    "company_name": '',
                    "type": '',
                    "start_date": '',
                    "end_date": '',
                    "title": '',
                    "hits": '',
                    "price_type": '',
                    "email": '',
                    "level_cd": '',
                    "gen": '',
                    "sns_code": '',
                    "ref_tel": '',
                    "company_tel": '',
                    "phone_number": '',
                    "tel": '',
                    "corp_ids": '',
                    "status_arr": '',
                    "data_type_arr": '',
                    "category_arr": '',
                    "not_corp_ids": '',
                    "page_num": '',
                    "page_size": '',
                    "total_size": '',
                    "category_id": "CA000007",
                    "category_name": "물류/교통",
                    "parent_id": '',
                    "grade": "7",
                    "corp_id": '',
                    "category_ids": '',
                    "category_nms": '',
                    "grades": ''
                },
                {
                    "product_id": '',
                    "creator_user_id": '',
                    "modified_user_id": '',
                    "user_id": '',
                    "contents_id": '',
                    "seq_id": '',
                    "status": "active",
                    "created_date": '',
                    "modified_date": '',
                    "search_type": '',
                    "search_keyword": '',
                    "company_name": '',
                    "type": '',
                    "start_date": '',
                    "end_date": '',
                    "title": '',
                    "hits": '',
                    "price_type": '',
                    "email": '',
                    "level_cd": '',
                    "gen": '',
                    "sns_code": '',
                    "ref_tel": '',
                    "company_tel": '',
                    "phone_number": '',
                    "tel": '',
                    "corp_ids": '',
                    "status_arr": '',
                    "data_type_arr": '',
                    "category_arr": '',
                    "not_corp_ids": '',
                    "page_num": '',
                    "page_size": '',
                    "total_size": '',
                    "category_id": "CA000008",
                    "category_name": "보건의료",
                    "parent_id": '',
                    "grade": "8",
                    "corp_id": '',
                    "category_ids": '',
                    "category_nms": '',
                    "grades": ''
                },
                {
                    "product_id": '',
                    "creator_user_id": '',
                    "modified_user_id": '',
                    "user_id": '',
                    "contents_id": '',
                    "seq_id": '',
                    "status": "active",
                    "created_date": '',
                    "modified_date": '',
                    "search_type": '',
                    "search_keyword": '',
                    "company_name": '',
                    "type": '',
                    "start_date": '',
                    "end_date": '',
                    "title": '',
                    "hits": '',
                    "price_type": '',
                    "email": '',
                    "level_cd": '',
                    "gen": '',
                    "sns_code": '',
                    "ref_tel": '',
                    "company_tel": '',
                    "phone_number": '',
                    "tel": '',
                    "corp_ids": '',
                    "status_arr": '',
                    "data_type_arr": '',
                    "category_arr": '',
                    "not_corp_ids": '',
                    "page_num": '',
                    "page_size": '',
                    "total_size": '',
                    "category_id": "CA000009",
                    "category_name": "부동산/지리",
                    "parent_id": '',
                    "grade": "9",
                    "corp_id": '',
                    "category_ids": '',
                    "category_nms": '',
                    "grades": ''
                },
                {
                    "product_id": '',
                    "creator_user_id": '',
                    "modified_user_id": '',
                    "user_id": '',
                    "contents_id": '',
                    "seq_id": '',
                    "status": "active",
                    "created_date": '',
                    "modified_date": '',
                    "search_type": '',
                    "search_keyword": '',
                    "company_name": '',
                    "type": '',
                    "start_date": '',
                    "end_date": '',
                    "title": '',
                    "hits": '',
                    "price_type": '',
                    "email": '',
                    "level_cd": '',
                    "gen": '',
                    "sns_code": '',
                    "ref_tel": '',
                    "company_tel": '',
                    "phone_number": '',
                    "tel": '',
                    "corp_ids": '',
                    "status_arr": '',
                    "data_type_arr": '',
                    "category_arr": '',
                    "not_corp_ids": '',
                    "page_num": '',
                    "page_size": '',
                    "total_size": '',
                    "category_id": "CA000010",
                    "category_name": "자동차",
                    "parent_id": '',
                    "grade": "10",
                    "corp_id": '',
                    "category_ids": '',
                    "category_nms": '',
                    "grades": ''
                },
                {
                    "product_id": '',
                    "creator_user_id": '',
                    "modified_user_id": '',
                    "user_id": '',
                    "contents_id": '',
                    "seq_id": '',
                    "status": "active",
                    "created_date": '',
                    "modified_date": '',
                    "search_type": '',
                    "search_keyword": '',
                    "company_name": '',
                    "type": '',
                    "start_date": '',
                    "end_date": '',
                    "title": '',
                    "hits": '',
                    "price_type": '',
                    "email": '',
                    "level_cd": '',
                    "gen": '',
                    "sns_code": '',
                    "ref_tel": '',
                    "company_tel": '',
                    "phone_number": '',
                    "tel": '',
                    "corp_ids": '',
                    "status_arr": '',
                    "data_type_arr": '',
                    "category_arr": '',
                    "not_corp_ids": '',
                    "page_num": '',
                    "page_size": '',
                    "total_size": '',
                    "category_id": "CA000011",
                    "category_name": "여가/레저",
                    "parent_id": '',
                    "grade": "11",
                    "corp_id": '',
                    "category_ids": '',
                    "category_nms": '',
                    "grades": ''
                },
                {
                    "product_id": '',
                    "creator_user_id": '',
                    "modified_user_id": '',
                    "user_id": '',
                    "contents_id": '',
                    "seq_id": '',
                    "status": "active",
                    "created_date": '',
                    "modified_date": '',
                    "search_type": '',
                    "search_keyword": '',
                    "company_name": '',
                    "type": '',
                    "start_date": '',
                    "end_date": '',
                    "title": '',
                    "hits": '',
                    "price_type": '',
                    "email": '',
                    "level_cd": '',
                    "gen": '',
                    "sns_code": '',
                    "ref_tel": '',
                    "company_tel": '',
                    "phone_number": '',
                    "tel": '',
                    "corp_ids": '',
                    "status_arr": '',
                    "data_type_arr": '',
                    "category_arr": '',
                    "not_corp_ids": '',
                    "page_num": '',
                    "page_size": '',
                    "total_size": '',
                    "category_id": "CA000012",
                    "category_name": "인공지능",
                    "parent_id": '',
                    "grade": "12",
                    "corp_id": '',
                    "category_ids": '',
                    "category_nms": '',
                    "grades": ''
                },
                {
                    "product_id": '',
                    "creator_user_id": '',
                    "modified_user_id": '',
                    "user_id": '',
                    "contents_id": '',
                    "seq_id": '',
                    "status": "active",
                    "created_date": '',
                    "modified_date": '',
                    "search_type": '',
                    "search_keyword": '',
                    "company_name": '',
                    "type": '',
                    "start_date": '',
                    "end_date": '',
                    "title": '',
                    "hits": '',
                    "price_type": '',
                    "email": '',
                    "level_cd": '',
                    "gen": '',
                    "sns_code": '',
                    "ref_tel": '',
                    "company_tel": '',
                    "phone_number": '',
                    "tel": '',
                    "corp_ids": '',
                    "status_arr": '',
                    "data_type_arr": '',
                    "category_arr": '',
                    "not_corp_ids": '',
                    "page_num": '',
                    "page_size": '',
                    "total_size": '',
                    "category_id": "CA000013",
                    "category_name": "SNS",
                    "parent_id": '',
                    "grade": "13",
                    "corp_id": '',
                    "category_ids": '',
                    "category_nms": '',
                    "grades": ''
                },
                {
                    "product_id": '',
                    "creator_user_id": '',
                    "modified_user_id": '',
                    "user_id": '',
                    "contents_id": '',
                    "seq_id": '',
                    "status": "active",
                    "created_date": '',
                    "modified_date": '',
                    "search_type": '',
                    "search_keyword": '',
                    "company_name": '',
                    "type": '',
                    "start_date": '',
                    "end_date": '',
                    "title": '',
                    "hits": '',
                    "price_type": '',
                    "email": '',
                    "level_cd": '',
                    "gen": '',
                    "sns_code": '',
                    "ref_tel": '',
                    "company_tel": '',
                    "phone_number": '',
                    "tel": '',
                    "corp_ids": '',
                    "status_arr": '',
                    "data_type_arr": '',
                    "category_arr": '',
                    "not_corp_ids": '',
                    "page_num": '',
                    "page_size": '',
                    "total_size": '',
                    "category_id": "CA000014",
                    "category_name": "미디어",
                    "parent_id": '',
                    "grade": "14",
                    "corp_id": '',
                    "category_ids": '',
                    "category_nms": '',
                    "grades": ''
                },
                {
                    "product_id": '',
                    "creator_user_id": '',
                    "modified_user_id": '',
                    "user_id": '',
                    "contents_id": '',
                    "seq_id": '',
                    "status": "active",
                    "created_date": '',
                    "modified_date": '',
                    "search_type": '',
                    "search_keyword": '',
                    "company_name": '',
                    "type": '',
                    "start_date": '',
                    "end_date": '',
                    "title": '',
                    "hits": '',
                    "price_type": '',
                    "email": '',
                    "level_cd": '',
                    "gen": '',
                    "sns_code": '',
                    "ref_tel": '',
                    "company_tel": '',
                    "phone_number": '',
                    "tel": '',
                    "corp_ids": '',
                    "status_arr": '',
                    "data_type_arr": '',
                    "category_arr": '',
                    "not_corp_ids": '',
                    "page_num": '',
                    "page_size": '',
                    "total_size": '',
                    "category_id": "CA000015",
                    "category_name": "공공데이터",
                    "parent_id": '',
                    "grade": "15",
                    "corp_id": '',
                    "category_ids": '',
                    "category_nms": '',
                    "grades": ''
                }
            ]
        }
    }

@app.get("/company/list",tags=["company"])
async def company_list():
    return {
        "code": "200",
        "data": [
            {
                "product_id": '',
                "creator_user_id": '',
                "modified_user_id": '',
                "user_id": '',
                "contents_id": '',
                "seq_id": '',
                "status": '',
                "created_date": '',
                "modified_date": '',
                "search_type": '',
                "search_keyword": '',
                "company_name": "MBN",
                "type": '',
                "start_date": '',
                "end_date": '',
                "title": '',
                "hits": '',
                "price_type": '',
                "email": '',
                "level_cd": '',
                "gen": '',
                "sns_code": '',
                "ref_tel": '',
                "company_tel": '',
                "phone_number": '',
                "tel": '',
                "corp_ids": '',
                "status_arr": '',
                "data_type_arr": '',
                "category_arr": '',
                "not_corp_ids": '',
                "page_num": '',
                "page_size": '',
                "total_size": '',
                "account": '',
                "password": '',
                "fullname": '',
                "root_id": '',
                "parent_id": '',
                "department": '',
                "position": '',
                "interest_category": '',
                "auth_type": '',
                "auth_value": '',
                "payment_id": '',
                "login_count": '',
                "password_update": '',
                "app_token": '',
                "company_logo": '',
                "company_site": '',
                "bank_name": '',
                "account_name": '',
                "account_number": '',
                "seller_status": '',
                "seller_id": '',
                "reset_code": '',
                "coupon_code": '',
                "return_code": '',
                "device_type": '',
                "req_seq": '',
                "res_seq": '',
                "confirm_datetime": '',
                "withdraw_date": '',
                "occupation": '',
                "expired_date": '',
                "auto_login": '',
                "discount": '',
                "email_yn": '',
                "sms_yn": '',
                "ref_name": '',
                "ref_company_name": '',
                "tdi_token": '',
                "mk_token": '',
                "mk_s_id": '',
                "report_yn": '',
                "expired_start_date": '',
                "expired_end_date": '',
                "confirm_id": '',
                "corp_id": "CORP000001",
                "corp_cd": "01",
                "corp_nm": '',
                "corp_logo_img": "companyLogo/2023_02_06_152319_MBN 로고 (PNG).png",
                "company_logo_file": '',
                "page_name": '',
                "corp_prof_inf": '',
                "corp_sup_data": '',
                "corp_sup_data_inf": '',
                "secsn_reason_cd": '',
                "secsn_reason_desc": '',
                "crt_dt": '',
                "crt_usr_id": '',
                "mdfy_dt": '',
                "mdfy_usr_id": '',
                "seq": '',
                "description": '',
                "product_cnt": '',
                "check_code": ''
            },
            {
                "product_id": '',
                "creator_user_id": '',
                "modified_user_id": '',
                "user_id": '',
                "contents_id": '',
                "seq_id": '',
                "status": '',
                "created_date": '',
                "modified_date": '',
                "search_type": '',
                "search_keyword": '',
                "company_name": "KDX한국데이터거래소",
                "type": '',
                "start_date": '',
                "end_date": '',
                "title": '',
                "hits": '',
                "price_type": '',
                "email": '',
                "level_cd": '',
                "gen": '',
                "sns_code": '',
                "ref_tel": '',
                "company_tel": '',
                "phone_number": '',
                "tel": '',
                "corp_ids": '',
                "status_arr": '',
                "data_type_arr": '',
                "category_arr": '',
                "not_corp_ids": '',
                "page_num": '',
                "page_size": '',
                "total_size": '',
                "account": '',
                "password": '',
                "fullname": '',
                "root_id": '',
                "parent_id": '',
                "department": '',
                "position": '',
                "interest_category": '',
                "auth_type": '',
                "auth_value": '',
                "payment_id": '',
                "login_count": '',
                "password_update": '',
                "app_token": '',
                "company_logo": '',
                "company_site": '',
                "bank_name": '',
                "account_name": '',
                "account_number": '',
                "seller_status": '',
                "seller_id": '',
                "reset_code": '',
                "coupon_code": '',
                "return_code": '',
                "device_type": '',
                "req_seq": '',
                "res_seq": '',
                "confirm_datetime": '',
                "withdraw_date": '',
                "occupation": '',
                "expired_date": '',
                "auto_login": '',
                "discount": '',
                "email_yn": '',
                "sms_yn": '',
                "ref_name": '',
                "ref_company_name": '',
                "tdi_token": '',
                "mk_token": '',
                "mk_s_id": '',
                "report_yn": '',
                "expired_start_date": '',
                "expired_end_date": '',
                "confirm_id": '',
                "corp_id": "CORP000007",
                "corp_cd": "08",
                "corp_nm": '',
                "corp_logo_img": "companyLogo/2022_03_18_014617_KDX한국데이터거래소 국문 가로(2).png",
                "company_logo_file": '',
                "page_name": '',
                "corp_prof_inf": '',
                "corp_sup_data": '',
                "corp_sup_data_inf": '',
                "secsn_reason_cd": '',
                "secsn_reason_desc": '',
                "crt_dt": '',
                "crt_usr_id": '',
                "mdfy_dt": '',
                "mdfy_usr_id": '',
                "seq": '',
                "description": '',
                "product_cnt": '',
                "check_code": ''
            },
            {
                "product_id": '',
                "creator_user_id": '',
                "modified_user_id": '',
                "user_id": '',
                "contents_id": '',
                "seq_id": '',
                "status": '',
                "created_date": '',
                "modified_date": '',
                "search_type": '',
                "search_keyword": '',
                "company_name": "CJ올리브네트웍스",
                "type": '',
                "start_date": '',
                "end_date": '',
                "title": '',
                "hits": '',
                "price_type": '',
                "email": '',
                "level_cd": '',
                "gen": '',
                "sns_code": '',
                "ref_tel": '',
                "company_tel": '',
                "phone_number": '',
                "tel": '',
                "corp_ids": '',
                "status_arr": '',
                "data_type_arr": '',
                "category_arr": '',
                "not_corp_ids": '',
                "page_num": '',
                "page_size": '',
                "total_size": '',
                "account": '',
                "password": '',
                "fullname": '',
                "root_id": '',
                "parent_id": '',
                "department": '',
                "position": '',
                "interest_category": '',
                "auth_type": '',
                "auth_value": '',
                "payment_id": '',
                "login_count": '',
                "password_update": '',
                "app_token": '',
                "company_logo": '',
                "company_site": '',
                "bank_name": '',
                "account_name": '',
                "account_number": '',
                "seller_status": '',
                "seller_id": '',
                "reset_code": '',
                "coupon_code": '',
                "return_code": '',
                "device_type": '',
                "req_seq": '',
                "res_seq": '',
                "confirm_datetime": '',
                "withdraw_date": '',
                "occupation": '',
                "expired_date": '',
                "auto_login": '',
                "discount": '',
                "email_yn": '',
                "sms_yn": '',
                "ref_name": '',
                "ref_company_name": '',
                "tdi_token": '',
                "mk_token": '',
                "mk_s_id": '',
                "report_yn": '',
                "expired_start_date": '',
                "expired_end_date": '',
                "confirm_id": '',
                "corp_id": "CORP000003",
                "corp_cd": "03",
                "corp_nm": '',
                "corp_logo_img": "companyLogo/img-logo-cj-s.png",
                "company_logo_file": '',
                "page_name": '',
                "corp_prof_inf": '',
                "corp_sup_data": '',
                "corp_sup_data_inf": '',
                "secsn_reason_cd": '',
                "secsn_reason_desc": '',
                "crt_dt": '',
                "crt_usr_id": '',
                "mdfy_dt": '',
                "mdfy_usr_id": '',
                "seq": '',
                "description": '',
                "product_cnt": '',
                "check_code": ''
            },
            {
                "product_id": '',
                "creator_user_id": '',
                "modified_user_id": '',
                "user_id": '',
                "contents_id": '',
                "seq_id": '',
                "status": '',
                "created_date": '',
                "modified_date": '',
                "search_type": '',
                "search_keyword": '',
                "company_name": "KB캐피탈",
                "type": '',
                "start_date": '',
                "end_date": '',
                "title": '',
                "hits": '',
                "price_type": '',
                "email": '',
                "level_cd": '',
                "gen": '',
                "sns_code": '',
                "ref_tel": '',
                "company_tel": '',
                "phone_number": '',
                "tel": '',
                "corp_ids": '',
                "status_arr": '',
                "data_type_arr": '',
                "category_arr": '',
                "not_corp_ids": '',
                "page_num": '',
                "page_size": '',
                "total_size": '',
                "account": '',
                "password": '',
                "fullname": '',
                "root_id": '',
                "parent_id": '',
                "department": '',
                "position": '',
                "interest_category": '',
                "auth_type": '',
                "auth_value": '',
                "payment_id": '',
                "login_count": '',
                "password_update": '',
                "app_token": '',
                "company_logo": '',
                "company_site": '',
                "bank_name": '',
                "account_name": '',
                "account_number": '',
                "seller_status": '',
                "seller_id": '',
                "reset_code": '',
                "coupon_code": '',
                "return_code": '',
                "device_type": '',
                "req_seq": '',
                "res_seq": '',
                "confirm_datetime": '',
                "withdraw_date": '',
                "occupation": '',
                "expired_date": '',
                "auto_login": '',
                "discount": '',
                "email_yn": '',
                "sms_yn": '',
                "ref_name": '',
                "ref_company_name": '',
                "tdi_token": '',
                "mk_token": '',
                "mk_s_id": '',
                "report_yn": '',
                "expired_start_date": '',
                "expired_end_date": '',
                "confirm_id": '',
                "corp_id": "CORP000023",
                "corp_cd": "35",
                "corp_nm": '',
                "corp_logo_img": "companyLogo/img-logo-coop-kb.png",
                "company_logo_file": '',
                "page_name": '',
                "corp_prof_inf": '',
                "corp_sup_data": '',
                "corp_sup_data_inf": '',
                "secsn_reason_cd": '',
                "secsn_reason_desc": '',
                "crt_dt": '',
                "crt_usr_id": '',
                "mdfy_dt": '',
                "mdfy_usr_id": '',
                "seq": '',
                "description": '',
                "product_cnt": '',
                "check_code": ''
            },
            {
                "product_id": '',
                "creator_user_id": '',
                "modified_user_id": '',
                "user_id": '',
                "contents_id": '',
                "seq_id": '',
                "status": '',
                "created_date": '',
                "modified_date": '',
                "search_type": '',
                "search_keyword": '',
                "company_name": "SK텔레콤",
                "type": '',
                "start_date": '',
                "end_date": '',
                "title": '',
                "hits": '',
                "price_type": '',
                "email": '',
                "level_cd": '',
                "gen": '',
                "sns_code": '',
                "ref_tel": '',
                "company_tel": '',
                "phone_number": '',
                "tel": '',
                "corp_ids": '',
                "status_arr": '',
                "data_type_arr": '',
                "category_arr": '',
                "not_corp_ids": '',
                "page_num": '',
                "page_size": '',
                "total_size": '',
                "account": '',
                "password": '',
                "fullname": '',
                "root_id": '',
                "parent_id": '',
                "department": '',
                "position": '',
                "interest_category": '',
                "auth_type": '',
                "auth_value": '',
                "payment_id": '',
                "login_count": '',
                "password_update": '',
                "app_token": '',
                "company_logo": '',
                "company_site": '',
                "bank_name": '',
                "account_name": '',
                "account_number": '',
                "seller_status": '',
                "seller_id": '',
                "reset_code": '',
                "coupon_code": '',
                "return_code": '',
                "device_type": '',
                "req_seq": '',
                "res_seq": '',
                "confirm_datetime": '',
                "withdraw_date": '',
                "occupation": '',
                "expired_date": '',
                "auto_login": '',
                "discount": '',
                "email_yn": '',
                "sms_yn": '',
                "ref_name": '',
                "ref_company_name": '',
                "tdi_token": '',
                "mk_token": '',
                "mk_s_id": '',
                "report_yn": '',
                "expired_start_date": '',
                "expired_end_date": '',
                "confirm_id": '',
                "corp_id": "CORP000004",
                "corp_cd": "04",
                "corp_nm": '',
                "corp_logo_img": "companyLogo/img-logo-skt-s.png",
                "company_logo_file": '',
                "page_name": '',
                "corp_prof_inf": '',
                "corp_sup_data": '',
                "corp_sup_data_inf": '',
                "secsn_reason_cd": '',
                "secsn_reason_desc": '',
                "crt_dt": '',
                "crt_usr_id": '',
                "mdfy_dt": '',
                "mdfy_usr_id": '',
                "seq": '',
                "description": '',
                "product_cnt": '',
                "check_code": ''
            },
            {
                "product_id": '',
                "creator_user_id": '',
                "modified_user_id": '',
                "user_id": '',
                "contents_id": '',
                "seq_id": '',
                "status": '',
                "created_date": '',
                "modified_date": '',
                "search_type": '',
                "search_keyword": '',
                "company_name": "경동도시가스",
                "type": '',
                "start_date": '',
                "end_date": '',
                "title": '',
                "hits": '',
                "price_type": '',
                "email": '',
                "level_cd": '',
                "gen": '',
                "sns_code": '',
                "ref_tel": '',
                "company_tel": '',
                "phone_number": '',
                "tel": '',
                "corp_ids": '',
                "status_arr": '',
                "data_type_arr": '',
                "category_arr": '',
                "not_corp_ids": '',
                "page_num": '',
                "page_size": '',
                "total_size": '',
                "account": '',
                "password": '',
                "fullname": '',
                "root_id": '',
                "parent_id": '',
                "department": '',
                "position": '',
                "interest_category": '',
                "auth_type": '',
                "auth_value": '',
                "payment_id": '',
                "login_count": '',
                "password_update": '',
                "app_token": '',
                "company_logo": '',
                "company_site": '',
                "bank_name": '',
                "account_name": '',
                "account_number": '',
                "seller_status": '',
                "seller_id": '',
                "reset_code": '',
                "coupon_code": '',
                "return_code": '',
                "device_type": '',
                "req_seq": '',
                "res_seq": '',
                "confirm_datetime": '',
                "withdraw_date": '',
                "occupation": '',
                "expired_date": '',
                "auto_login": '',
                "discount": '',
                "email_yn": '',
                "sms_yn": '',
                "ref_name": '',
                "ref_company_name": '',
                "tdi_token": '',
                "mk_token": '',
                "mk_s_id": '',
                "report_yn": '',
                "expired_start_date": '',
                "expired_end_date": '',
                "confirm_id": '',
                "corp_id": "CORP000016",
                "corp_cd": "19",
                "corp_nm": '',
                "corp_logo_img": "companyLogo/2022_04_13_152738_시그니처_좌우조합_국영문 로고타입.png",
                "company_logo_file": '',
                "page_name": '',
                "corp_prof_inf": '',
                "corp_sup_data": '',
                "corp_sup_data_inf": '',
                "secsn_reason_cd": '',
                "secsn_reason_desc": '',
                "crt_dt": '',
                "crt_usr_id": '',
                "mdfy_dt": '',
                "mdfy_usr_id": '',
                "seq": '',
                "description": '',
                "product_cnt": '',
                "check_code": ''
            },
            {
                "product_id": '',
                "creator_user_id": '',
                "modified_user_id": '',
                "user_id": '',
                "contents_id": '',
                "seq_id": '',
                "status": '',
                "created_date": '',
                "modified_date": '',
                "search_type": '',
                "search_keyword": '',
                "company_name": "나이스디앤알",
                "type": '',
                "start_date": '',
                "end_date": '',
                "title": '',
                "hits": '',
                "price_type": '',
                "email": '',
                "level_cd": '',
                "gen": '',
                "sns_code": '',
                "ref_tel": '',
                "company_tel": '',
                "phone_number": '',
                "tel": '',
                "corp_ids": '',
                "status_arr": '',
                "data_type_arr": '',
                "category_arr": '',
                "not_corp_ids": '',
                "page_num": '',
                "page_size": '',
                "total_size": '',
                "account": '',
                "password": '',
                "fullname": '',
                "root_id": '',
                "parent_id": '',
                "department": '',
                "position": '',
                "interest_category": '',
                "auth_type": '',
                "auth_value": '',
                "payment_id": '',
                "login_count": '',
                "password_update": '',
                "app_token": '',
                "company_logo": '',
                "company_site": '',
                "bank_name": '',
                "account_name": '',
                "account_number": '',
                "seller_status": '',
                "seller_id": '',
                "reset_code": '',
                "coupon_code": '',
                "return_code": '',
                "device_type": '',
                "req_seq": '',
                "res_seq": '',
                "confirm_datetime": '',
                "withdraw_date": '',
                "occupation": '',
                "expired_date": '',
                "auto_login": '',
                "discount": '',
                "email_yn": '',
                "sms_yn": '',
                "ref_name": '',
                "ref_company_name": '',
                "tdi_token": '',
                "mk_token": '',
                "mk_s_id": '',
                "report_yn": '',
                "expired_start_date": '',
                "expired_end_date": '',
                "confirm_id": '',
                "corp_id": "CORP000008",
                "corp_cd": "09",
                "corp_nm": '',
                "corp_logo_img": "companyLogo/img-logo-nice-s.png",
                "company_logo_file": '',
                "page_name": '',
                "corp_prof_inf": '',
                "corp_sup_data": '',
                "corp_sup_data_inf": '',
                "secsn_reason_cd": '',
                "secsn_reason_desc": '',
                "crt_dt": '',
                "crt_usr_id": '',
                "mdfy_dt": '',
                "mdfy_usr_id": '',
                "seq": '',
                "description": '',
                "product_cnt": '',
                "check_code": ''
            },
            {
                "product_id": '',
                "creator_user_id": '',
                "modified_user_id": '',
                "user_id": '',
                "contents_id": '',
                "seq_id": '',
                "status": '',
                "created_date": '',
                "modified_date": '',
                "search_type": '',
                "search_keyword": '',
                "company_name": "농협은행(농협카드)",
                "type": '',
                "start_date": '',
                "end_date": '',
                "title": '',
                "hits": '',
                "price_type": '',
                "email": '',
                "level_cd": '',
                "gen": '',
                "sns_code": '',
                "ref_tel": '',
                "company_tel": '',
                "phone_number": '',
                "tel": '',
                "corp_ids": '',
                "status_arr": '',
                "data_type_arr": '',
                "category_arr": '',
                "not_corp_ids": '',
                "page_num": '',
                "page_size": '',
                "total_size": '',
                "account": '',
                "password": '',
                "fullname": '',
                "root_id": '',
                "parent_id": '',
                "department": '',
                "position": '',
                "interest_category": '',
                "auth_type": '',
                "auth_value": '',
                "payment_id": '',
                "login_count": '',
                "password_update": '',
                "app_token": '',
                "company_logo": '',
                "company_site": '',
                "bank_name": '',
                "account_name": '',
                "account_number": '',
                "seller_status": '',
                "seller_id": '',
                "reset_code": '',
                "coupon_code": '',
                "return_code": '',
                "device_type": '',
                "req_seq": '',
                "res_seq": '',
                "confirm_datetime": '',
                "withdraw_date": '',
                "occupation": '',
                "expired_date": '',
                "auto_login": '',
                "discount": '',
                "email_yn": '',
                "sms_yn": '',
                "ref_name": '',
                "ref_company_name": '',
                "tdi_token": '',
                "mk_token": '',
                "mk_s_id": '',
                "report_yn": '',
                "expired_start_date": '',
                "expired_end_date": '',
                "confirm_id": '',
                "corp_id": "CORP000024",
                "corp_cd": "38",
                "corp_nm": '',
                "corp_logo_img": "companyLogo/img-logo-nhbank.jpg",
                "company_logo_file": '',
                "page_name": '',
                "corp_prof_inf": '',
                "corp_sup_data": '',
                "corp_sup_data_inf": '',
                "secsn_reason_cd": '',
                "secsn_reason_desc": '',
                "crt_dt": '',
                "crt_usr_id": '',
                "mdfy_dt": '',
                "mdfy_usr_id": '',
                "seq": '',
                "description": '',
                "product_cnt": '',
                "check_code": ''
            },
            {
                "product_id": '',
                "creator_user_id": '',
                "modified_user_id": '',
                "user_id": '',
                "contents_id": '',
                "seq_id": '',
                "status": '',
                "created_date": '',
                "modified_date": '',
                "search_type": '',
                "search_keyword": '',
                "company_name": "삼성카드",
                "type": '',
                "start_date": '',
                "end_date": '',
                "title": '',
                "hits": '',
                "price_type": '',
                "email": '',
                "level_cd": '',
                "gen": '',
                "sns_code": '',
                "ref_tel": '',
                "company_tel": '',
                "phone_number": '',
                "tel": '',
                "corp_ids": '',
                "status_arr": '',
                "data_type_arr": '',
                "category_arr": '',
                "not_corp_ids": '',
                "page_num": '',
                "page_size": '',
                "total_size": '',
                "account": '',
                "password": '',
                "fullname": '',
                "root_id": '',
                "parent_id": '',
                "department": '',
                "position": '',
                "interest_category": '',
                "auth_type": '',
                "auth_value": '',
                "payment_id": '',
                "login_count": '',
                "password_update": '',
                "app_token": '',
                "company_logo": '',
                "company_site": '',
                "bank_name": '',
                "account_name": '',
                "account_number": '',
                "seller_status": '',
                "seller_id": '',
                "reset_code": '',
                "coupon_code": '',
                "return_code": '',
                "device_type": '',
                "req_seq": '',
                "res_seq": '',
                "confirm_datetime": '',
                "withdraw_date": '',
                "occupation": '',
                "expired_date": '',
                "auto_login": '',
                "discount": '',
                "email_yn": '',
                "sms_yn": '',
                "ref_name": '',
                "ref_company_name": '',
                "tdi_token": '',
                "mk_token": '',
                "mk_s_id": '',
                "report_yn": '',
                "expired_start_date": '',
                "expired_end_date": '',
                "confirm_id": '',
                "corp_id": "CORP000002",
                "corp_cd": "02",
                "corp_nm": '',
                "corp_logo_img": "companyLogo/2022_06_30_171850_Samsungcard CI_KDX.png",
                "company_logo_file": '',
                "page_name": '',
                "corp_prof_inf": '',
                "corp_sup_data": '',
                "corp_sup_data_inf": '',
                "secsn_reason_cd": '',
                "secsn_reason_desc": '',
                "crt_dt": '',
                "crt_usr_id": '',
                "mdfy_dt": '',
                "mdfy_usr_id": '',
                "seq": '',
                "description": '',
                "product_cnt": '',
                "check_code": ''
            },
            {
                "product_id": '',
                "creator_user_id": '',
                "modified_user_id": '',
                "user_id": '',
                "contents_id": '',
                "seq_id": '',
                "status": '',
                "created_date": '',
                "modified_date": '',
                "search_type": '',
                "search_keyword": '',
                "company_name": "식신",
                "type": '',
                "start_date": '',
                "end_date": '',
                "title": '',
                "hits": '',
                "price_type": '',
                "email": '',
                "level_cd": '',
                "gen": '',
                "sns_code": '',
                "ref_tel": '',
                "company_tel": '',
                "phone_number": '',
                "tel": '',
                "corp_ids": '',
                "status_arr": '',
                "data_type_arr": '',
                "category_arr": '',
                "not_corp_ids": '',
                "page_num": '',
                "page_size": '',
                "total_size": '',
                "account": '',
                "password": '',
                "fullname": '',
                "root_id": '',
                "parent_id": '',
                "department": '',
                "position": '',
                "interest_category": '',
                "auth_type": '',
                "auth_value": '',
                "payment_id": '',
                "login_count": '',
                "password_update": '',
                "app_token": '',
                "company_logo": '',
                "company_site": '',
                "bank_name": '',
                "account_name": '',
                "account_number": '',
                "seller_status": '',
                "seller_id": '',
                "reset_code": '',
                "coupon_code": '',
                "return_code": '',
                "device_type": '',
                "req_seq": '',
                "res_seq": '',
                "confirm_datetime": '',
                "withdraw_date": '',
                "occupation": '',
                "expired_date": '',
                "auto_login": '',
                "discount": '',
                "email_yn": '',
                "sms_yn": '',
                "ref_name": '',
                "ref_company_name": '',
                "tdi_token": '',
                "mk_token": '',
                "mk_s_id": '',
                "report_yn": '',
                "expired_start_date": '',
                "expired_end_date": '',
                "confirm_id": '',
                "corp_id": "CORP000013",
                "corp_cd": "14",
                "corp_nm": '',
                "corp_logo_img": "companyLogo/2021_03_31_085356_img-logo-sicsin-s.png",
                "company_logo_file": '',
                "page_name": '',
                "corp_prof_inf": '',
                "corp_sup_data": '',
                "corp_sup_data_inf": '',
                "secsn_reason_cd": '',
                "secsn_reason_desc": '',
                "crt_dt": '',
                "crt_usr_id": '',
                "mdfy_dt": '',
                "mdfy_usr_id": '',
                "seq": '',
                "description": '',
                "product_cnt": '',
                "check_code": ''
            },
            {
                "product_id": '',
                "creator_user_id": '',
                "modified_user_id": '',
                "user_id": '',
                "contents_id": '',
                "seq_id": '',
                "status": '',
                "created_date": '',
                "modified_date": '',
                "search_type": '',
                "search_keyword": '',
                "company_name": "신한카드",
                "type": '',
                "start_date": '',
                "end_date": '',
                "title": '',
                "hits": '',
                "price_type": '',
                "email": '',
                "level_cd": '',
                "gen": '',
                "sns_code": '',
                "ref_tel": '',
                "company_tel": '',
                "phone_number": '',
                "tel": '',
                "corp_ids": '',
                "status_arr": '',
                "data_type_arr": '',
                "category_arr": '',
                "not_corp_ids": '',
                "page_num": '',
                "page_size": '',
                "total_size": '',
                "account": '',
                "password": '',
                "fullname": '',
                "root_id": '',
                "parent_id": '',
                "department": '',
                "position": '',
                "interest_category": '',
                "auth_type": '',
                "auth_value": '',
                "payment_id": '',
                "login_count": '',
                "password_update": '',
                "app_token": '',
                "company_logo": '',
                "company_site": '',
                "bank_name": '',
                "account_name": '',
                "account_number": '',
                "seller_status": '',
                "seller_id": '',
                "reset_code": '',
                "coupon_code": '',
                "return_code": '',
                "device_type": '',
                "req_seq": '',
                "res_seq": '',
                "confirm_datetime": '',
                "withdraw_date": '',
                "occupation": '',
                "expired_date": '',
                "auto_login": '',
                "discount": '',
                "email_yn": '',
                "sms_yn": '',
                "ref_name": '',
                "ref_company_name": '',
                "tdi_token": '',
                "mk_token": '',
                "mk_s_id": '',
                "report_yn": '',
                "expired_start_date": '',
                "expired_end_date": '',
                "confirm_id": '',
                "corp_id": "CORP000027",
                "corp_cd": "32",
                "corp_nm": '',
                "corp_logo_img": "companyLogo/img-logo-coop-shinhan.png",
                "company_logo_file": '',
                "page_name": '',
                "corp_prof_inf": '',
                "corp_sup_data": '',
                "corp_sup_data_inf": '',
                "secsn_reason_cd": '',
                "secsn_reason_desc": '',
                "crt_dt": '',
                "crt_usr_id": '',
                "mdfy_dt": '',
                "mdfy_usr_id": '',
                "seq": '',
                "description": '',
                "product_cnt": '',
                "check_code": ''
            },
            {
                "product_id": '',
                "creator_user_id": '',
                "modified_user_id": '',
                "user_id": '',
                "contents_id": '',
                "seq_id": '',
                "status": '',
                "created_date": '',
                "modified_date": '',
                "search_type": '',
                "search_keyword": '',
                "company_name": "써머스플랫폼",
                "type": '',
                "start_date": '',
                "end_date": '',
                "title": '',
                "hits": '',
                "price_type": '',
                "email": '',
                "level_cd": '',
                "gen": '',
                "sns_code": '',
                "ref_tel": '',
                "company_tel": '',
                "phone_number": '',
                "tel": '',
                "corp_ids": '',
                "status_arr": '',
                "data_type_arr": '',
                "category_arr": '',
                "not_corp_ids": '',
                "page_num": '',
                "page_size": '',
                "total_size": '',
                "account": '',
                "password": '',
                "fullname": '',
                "root_id": '',
                "parent_id": '',
                "department": '',
                "position": '',
                "interest_category": '',
                "auth_type": '',
                "auth_value": '',
                "payment_id": '',
                "login_count": '',
                "password_update": '',
                "app_token": '',
                "company_logo": '',
                "company_site": '',
                "bank_name": '',
                "account_name": '',
                "account_number": '',
                "seller_status": '',
                "seller_id": '',
                "reset_code": '',
                "coupon_code": '',
                "return_code": '',
                "device_type": '',
                "req_seq": '',
                "res_seq": '',
                "confirm_datetime": '',
                "withdraw_date": '',
                "occupation": '',
                "expired_date": '',
                "auto_login": '',
                "discount": '',
                "email_yn": '',
                "sms_yn": '',
                "ref_name": '',
                "ref_company_name": '',
                "tdi_token": '',
                "mk_token": '',
                "mk_s_id": '',
                "report_yn": '',
                "expired_start_date": '',
                "expired_end_date": '',
                "confirm_id": '',
                "corp_id": "CORP000046",
                "corp_cd": "53",
                "corp_nm": '',
                "corp_logo_img": "companyLogo/2023_02_18_101142_600x200_sp_eng.jpg",
                "company_logo_file": '',
                "page_name": '',
                "corp_prof_inf": '',
                "corp_sup_data": '',
                "corp_sup_data_inf": '',
                "secsn_reason_cd": '',
                "secsn_reason_desc": '',
                "crt_dt": '',
                "crt_usr_id": '',
                "mdfy_dt": '',
                "mdfy_usr_id": '',
                "seq": '',
                "description": '',
                "product_cnt": '',
                "check_code": ''
            },
            {
                "product_id": '',
                "creator_user_id": '',
                "modified_user_id": '',
                "user_id": '',
                "contents_id": '',
                "seq_id": '',
                "status": '',
                "created_date": '',
                "modified_date": '',
                "search_type": '',
                "search_keyword": '',
                "company_name": "엘지씨엔에스",
                "type": '',
                "start_date": '',
                "end_date": '',
                "title": '',
                "hits": '',
                "price_type": '',
                "email": '',
                "level_cd": '',
                "gen": '',
                "sns_code": '',
                "ref_tel": '',
                "company_tel": '',
                "phone_number": '',
                "tel": '',
                "corp_ids": '',
                "status_arr": '',
                "data_type_arr": '',
                "category_arr": '',
                "not_corp_ids": '',
                "page_num": '',
                "page_size": '',
                "total_size": '',
                "account": '',
                "password": '',
                "fullname": '',
                "root_id": '',
                "parent_id": '',
                "department": '',
                "position": '',
                "interest_category": '',
                "auth_type": '',
                "auth_value": '',
                "payment_id": '',
                "login_count": '',
                "password_update": '',
                "app_token": '',
                "company_logo": '',
                "company_site": '',
                "bank_name": '',
                "account_name": '',
                "account_number": '',
                "seller_status": '',
                "seller_id": '',
                "reset_code": '',
                "coupon_code": '',
                "return_code": '',
                "device_type": '',
                "req_seq": '',
                "res_seq": '',
                "confirm_datetime": '',
                "withdraw_date": '',
                "occupation": '',
                "expired_date": '',
                "auto_login": '',
                "discount": '',
                "email_yn": '',
                "sms_yn": '',
                "ref_name": '',
                "ref_company_name": '',
                "tdi_token": '',
                "mk_token": '',
                "mk_s_id": '',
                "report_yn": '',
                "expired_start_date": '',
                "expired_end_date": '',
                "confirm_id": '',
                "corp_id": "CORP000044",
                "corp_cd": "51",
                "corp_nm": '',
                "corp_logo_img": "companyLogo/2022_08_01_160450_LGCNS_가로조합(영).jpg",
                "company_logo_file": '',
                "page_name": '',
                "corp_prof_inf": '',
                "corp_sup_data": '',
                "corp_sup_data_inf": '',
                "secsn_reason_cd": '',
                "secsn_reason_desc": '',
                "crt_dt": '',
                "crt_usr_id": '',
                "mdfy_dt": '',
                "mdfy_usr_id": '',
                "seq": '',
                "description": '',
                "product_cnt": '',
                "check_code": ''
            },
            {
                "product_id": '',
                "creator_user_id": '',
                "modified_user_id": '',
                "user_id": '',
                "contents_id": '',
                "seq_id": '',
                "status": '',
                "created_date": '',
                "modified_date": '',
                "search_type": '',
                "search_keyword": '',
                "company_name": "엘지유플러스",
                "type": '',
                "start_date": '',
                "end_date": '',
                "title": '',
                "hits": '',
                "price_type": '',
                "email": '',
                "level_cd": '',
                "gen": '',
                "sns_code": '',
                "ref_tel": '',
                "company_tel": '',
                "phone_number": '',
                "tel": '',
                "corp_ids": '',
                "status_arr": '',
                "data_type_arr": '',
                "category_arr": '',
                "not_corp_ids": '',
                "page_num": '',
                "page_size": '',
                "total_size": '',
                "account": '',
                "password": '',
                "fullname": '',
                "root_id": '',
                "parent_id": '',
                "department": '',
                "position": '',
                "interest_category": '',
                "auth_type": '',
                "auth_value": '',
                "payment_id": '',
                "login_count": '',
                "password_update": '',
                "app_token": '',
                "company_logo": '',
                "company_site": '',
                "bank_name": '',
                "account_name": '',
                "account_number": '',
                "seller_status": '',
                "seller_id": '',
                "reset_code": '',
                "coupon_code": '',
                "return_code": '',
                "device_type": '',
                "req_seq": '',
                "res_seq": '',
                "confirm_datetime": '',
                "withdraw_date": '',
                "occupation": '',
                "expired_date": '',
                "auto_login": '',
                "discount": '',
                "email_yn": '',
                "sms_yn": '',
                "ref_name": '',
                "ref_company_name": '',
                "tdi_token": '',
                "mk_token": '',
                "mk_s_id": '',
                "report_yn": '',
                "expired_start_date": '',
                "expired_end_date": '',
                "confirm_id": '',
                "corp_id": "CORP000030",
                "corp_cd": "36",
                "corp_nm": '',
                "corp_logo_img": "companyLogo/img-logo-coop-uplus.png",
                "company_logo_file": '',
                "page_name": '',
                "corp_prof_inf": '',
                "corp_sup_data": '',
                "corp_sup_data_inf": '',
                "secsn_reason_cd": '',
                "secsn_reason_desc": '',
                "crt_dt": '',
                "crt_usr_id": '',
                "mdfy_dt": '',
                "mdfy_usr_id": '',
                "seq": '',
                "description": '',
                "product_cnt": '',
                "check_code": ''
            },
            {
                "product_id": '',
                "creator_user_id": '',
                "modified_user_id": '',
                "user_id": '',
                "contents_id": '',
                "seq_id": '',
                "status": '',
                "created_date": '',
                "modified_date": '',
                "search_type": '',
                "search_keyword": '',
                "company_name": "웰컴에프앤디",
                "type": '',
                "start_date": '',
                "end_date": '',
                "title": '',
                "hits": '',
                "price_type": '',
                "email": '',
                "level_cd": '',
                "gen": '',
                "sns_code": '',
                "ref_tel": '',
                "company_tel": '',
                "phone_number": '',
                "tel": '',
                "corp_ids": '',
                "status_arr": '',
                "data_type_arr": '',
                "category_arr": '',
                "not_corp_ids": '',
                "page_num": '',
                "page_size": '',
                "total_size": '',
                "account": '',
                "password": '',
                "fullname": '',
                "root_id": '',
                "parent_id": '',
                "department": '',
                "position": '',
                "interest_category": '',
                "auth_type": '',
                "auth_value": '',
                "payment_id": '',
                "login_count": '',
                "password_update": '',
                "app_token": '',
                "company_logo": '',
                "company_site": '',
                "bank_name": '',
                "account_name": '',
                "account_number": '',
                "seller_status": '',
                "seller_id": '',
                "reset_code": '',
                "coupon_code": '',
                "return_code": '',
                "device_type": '',
                "req_seq": '',
                "res_seq": '',
                "confirm_datetime": '',
                "withdraw_date": '',
                "occupation": '',
                "expired_date": '',
                "auto_login": '',
                "discount": '',
                "email_yn": '',
                "sms_yn": '',
                "ref_name": '',
                "ref_company_name": '',
                "tdi_token": '',
                "mk_token": '',
                "mk_s_id": '',
                "report_yn": '',
                "expired_start_date": '',
                "expired_end_date": '',
                "confirm_id": '',
                "corp_id": "CORP000006",
                "corp_cd": "06",
                "corp_nm": '',
                "corp_logo_img": "companyLogo/img-logo-welcome-s.png",
                "company_logo_file": '',
                "page_name": '',
                "corp_prof_inf": '',
                "corp_sup_data": '',
                "corp_sup_data_inf": '',
                "secsn_reason_cd": '',
                "secsn_reason_desc": '',
                "crt_dt": '',
                "crt_usr_id": '',
                "mdfy_dt": '',
                "mdfy_usr_id": '',
                "seq": '',
                "description": '',
                "product_cnt": '',
                "check_code": ''
            },
            {
                "product_id": '',
                "creator_user_id": '',
                "modified_user_id": '',
                "user_id": '',
                "contents_id": '',
                "seq_id": '',
                "status": '',
                "created_date": '',
                "modified_date": '',
                "search_type": '',
                "search_keyword": '',
                "company_name": "윕스",
                "type": '',
                "start_date": '',
                "end_date": '',
                "title": '',
                "hits": '',
                "price_type": '',
                "email": '',
                "level_cd": '',
                "gen": '',
                "sns_code": '',
                "ref_tel": '',
                "company_tel": '',
                "phone_number": '',
                "tel": '',
                "corp_ids": '',
                "status_arr": '',
                "data_type_arr": '',
                "category_arr": '',
                "not_corp_ids": '',
                "page_num": '',
                "page_size": '',
                "total_size": '',
                "account": '',
                "password": '',
                "fullname": '',
                "root_id": '',
                "parent_id": '',
                "department": '',
                "position": '',
                "interest_category": '',
                "auth_type": '',
                "auth_value": '',
                "payment_id": '',
                "login_count": '',
                "password_update": '',
                "app_token": '',
                "company_logo": '',
                "company_site": '',
                "bank_name": '',
                "account_name": '',
                "account_number": '',
                "seller_status": '',
                "seller_id": '',
                "reset_code": '',
                "coupon_code": '',
                "return_code": '',
                "device_type": '',
                "req_seq": '',
                "res_seq": '',
                "confirm_datetime": '',
                "withdraw_date": '',
                "occupation": '',
                "expired_date": '',
                "auto_login": '',
                "discount": '',
                "email_yn": '',
                "sms_yn": '',
                "ref_name": '',
                "ref_company_name": '',
                "tdi_token": '',
                "mk_token": '',
                "mk_s_id": '',
                "report_yn": '',
                "expired_start_date": '',
                "expired_end_date": '',
                "confirm_id": '',
                "corp_id": "CORP000047",
                "corp_cd": "54",
                "corp_nm": '',
                "corp_logo_img": "companyLogo/2023_03_16_110837_기본형.png",
                "company_logo_file": '',
                "page_name": '',
                "corp_prof_inf": '',
                "corp_sup_data": '',
                "corp_sup_data_inf": '',
                "secsn_reason_cd": '',
                "secsn_reason_desc": '',
                "crt_dt": '',
                "crt_usr_id": '',
                "mdfy_dt": '',
                "mdfy_usr_id": '',
                "seq": '',
                "description": '',
                "product_cnt": '',
                "check_code": ''
            },
            {
                "product_id": '',
                "creator_user_id": '',
                "modified_user_id": '',
                "user_id": '',
                "contents_id": '',
                "seq_id": '',
                "status": '',
                "created_date": '',
                "modified_date": '',
                "search_type": '',
                "search_keyword": '',
                "company_name": "인사이트베슬",
                "type": '',
                "start_date": '',
                "end_date": '',
                "title": '',
                "hits": '',
                "price_type": '',
                "email": '',
                "level_cd": '',
                "gen": '',
                "sns_code": '',
                "ref_tel": '',
                "company_tel": '',
                "phone_number": '',
                "tel": '',
                "corp_ids": '',
                "status_arr": '',
                "data_type_arr": '',
                "category_arr": '',
                "not_corp_ids": '',
                "page_num": '',
                "page_size": '',
                "total_size": '',
                "account": '',
                "password": '',
                "fullname": '',
                "root_id": '',
                "parent_id": '',
                "department": '',
                "position": '',
                "interest_category": '',
                "auth_type": '',
                "auth_value": '',
                "payment_id": '',
                "login_count": '',
                "password_update": '',
                "app_token": '',
                "company_logo": '',
                "company_site": '',
                "bank_name": '',
                "account_name": '',
                "account_number": '',
                "seller_status": '',
                "seller_id": '',
                "reset_code": '',
                "coupon_code": '',
                "return_code": '',
                "device_type": '',
                "req_seq": '',
                "res_seq": '',
                "confirm_datetime": '',
                "withdraw_date": '',
                "occupation": '',
                "expired_date": '',
                "auto_login": '',
                "discount": '',
                "email_yn": '',
                "sms_yn": '',
                "ref_name": '',
                "ref_company_name": '',
                "tdi_token": '',
                "mk_token": '',
                "mk_s_id": '',
                "report_yn": '',
                "expired_start_date": '',
                "expired_end_date": '',
                "confirm_id": '',
                "corp_id": "CORP000045",
                "corp_cd": "52",
                "corp_nm": '',
                "corp_logo_img": "companyLogo/2022_10_19_164544_faviconPNG-01.png",
                "company_logo_file": '',
                "page_name": '',
                "corp_prof_inf": '',
                "corp_sup_data": '',
                "corp_sup_data_inf": '',
                "secsn_reason_cd": '',
                "secsn_reason_desc": '',
                "crt_dt": '',
                "crt_usr_id": '',
                "mdfy_dt": '',
                "mdfy_usr_id": '',
                "seq": '',
                "description": '',
                "product_cnt": '',
                "check_code": ''
            },
            {
                "product_id": '',
                "creator_user_id": '',
                "modified_user_id": '',
                "user_id": '',
                "contents_id": '',
                "seq_id": '',
                "status": '',
                "created_date": '',
                "modified_date": '',
                "search_type": '',
                "search_keyword": '',
                "company_name": "주식회사 위드365",
                "type": '',
                "start_date": '',
                "end_date": '',
                "title": '',
                "hits": '',
                "price_type": '',
                "email": '',
                "level_cd": '',
                "gen": '',
                "sns_code": '',
                "ref_tel": '',
                "company_tel": '',
                "phone_number": '',
                "tel": '',
                "corp_ids": '',
                "status_arr": '',
                "data_type_arr": '',
                "category_arr": '',
                "not_corp_ids": '',
                "page_num": '',
                "page_size": '',
                "total_size": '',
                "account": '',
                "password": '',
                "fullname": '',
                "root_id": '',
                "parent_id": '',
                "department": '',
                "position": '',
                "interest_category": '',
                "auth_type": '',
                "auth_value": '',
                "payment_id": '',
                "login_count": '',
                "password_update": '',
                "app_token": '',
                "company_logo": '',
                "company_site": '',
                "bank_name": '',
                "account_name": '',
                "account_number": '',
                "seller_status": '',
                "seller_id": '',
                "reset_code": '',
                "coupon_code": '',
                "return_code": '',
                "device_type": '',
                "req_seq": '',
                "res_seq": '',
                "confirm_datetime": '',
                "withdraw_date": '',
                "occupation": '',
                "expired_date": '',
                "auto_login": '',
                "discount": '',
                "email_yn": '',
                "sms_yn": '',
                "ref_name": '',
                "ref_company_name": '',
                "tdi_token": '',
                "mk_token": '',
                "mk_s_id": '',
                "report_yn": '',
                "expired_start_date": '',
                "expired_end_date": '',
                "confirm_id": '',
                "corp_id": "CORP000043",
                "corp_cd": "50",
                "corp_nm": '',
                "corp_logo_img": "companyLogo/2022_07_21_112130_KakaoTalk_20220721_095506530.png",
                "company_logo_file": '',
                "page_name": '',
                "corp_prof_inf": '',
                "corp_sup_data": '',
                "corp_sup_data_inf": '',
                "secsn_reason_cd": '',
                "secsn_reason_desc": '',
                "crt_dt": '',
                "crt_usr_id": '',
                "mdfy_dt": '',
                "mdfy_usr_id": '',
                "seq": '',
                "description": '',
                "product_cnt": '',
                "check_code": ''
            },
            {
                "product_id": '',
                "creator_user_id": '',
                "modified_user_id": '',
                "user_id": '',
                "contents_id": '',
                "seq_id": '',
                "status": '',
                "created_date": '',
                "modified_date": '',
                "search_type": '',
                "search_keyword": '',
                "company_name": "지에스리테일",
                "type": '',
                "start_date": '',
                "end_date": '',
                "title": '',
                "hits": '',
                "price_type": '',
                "email": '',
                "level_cd": '',
                "gen": '',
                "sns_code": '',
                "ref_tel": '',
                "company_tel": '',
                "phone_number": '',
                "tel": '',
                "corp_ids": '',
                "status_arr": '',
                "data_type_arr": '',
                "category_arr": '',
                "not_corp_ids": '',
                "page_num": '',
                "page_size": '',
                "total_size": '',
                "account": '',
                "password": '',
                "fullname": '',
                "root_id": '',
                "parent_id": '',
                "department": '',
                "position": '',
                "interest_category": '',
                "auth_type": '',
                "auth_value": '',
                "payment_id": '',
                "login_count": '',
                "password_update": '',
                "app_token": '',
                "company_logo": '',
                "company_site": '',
                "bank_name": '',
                "account_name": '',
                "account_number": '',
                "seller_status": '',
                "seller_id": '',
                "reset_code": '',
                "coupon_code": '',
                "return_code": '',
                "device_type": '',
                "req_seq": '',
                "res_seq": '',
                "confirm_datetime": '',
                "withdraw_date": '',
                "occupation": '',
                "expired_date": '',
                "auto_login": '',
                "discount": '',
                "email_yn": '',
                "sms_yn": '',
                "ref_name": '',
                "ref_company_name": '',
                "tdi_token": '',
                "mk_token": '',
                "mk_s_id": '',
                "report_yn": '',
                "expired_start_date": '',
                "expired_end_date": '',
                "confirm_id": '',
                "corp_id": "CORP000032",
                "corp_cd": "07",
                "corp_nm": '',
                "corp_logo_img": "companyLogo/img-logo-gsretail-s.png",
                "company_logo_file": '',
                "page_name": '',
                "corp_prof_inf": '',
                "corp_sup_data": '',
                "corp_sup_data_inf": '',
                "secsn_reason_cd": '',
                "secsn_reason_desc": '',
                "crt_dt": '',
                "crt_usr_id": '',
                "mdfy_dt": '',
                "mdfy_usr_id": '',
                "seq": '',
                "description": '',
                "product_cnt": '',
                "check_code": ''
            },
            {
                "product_id": '',
                "creator_user_id": '',
                "modified_user_id": '',
                "user_id": '',
                "contents_id": '',
                "seq_id": '',
                "status": '',
                "created_date": '',
                "modified_date": '',
                "search_type": '',
                "search_keyword": '',
                "company_name": "코리아크레딧뷰로",
                "type": '',
                "start_date": '',
                "end_date": '',
                "title": '',
                "hits": '',
                "price_type": '',
                "email": '',
                "level_cd": '',
                "gen": '',
                "sns_code": '',
                "ref_tel": '',
                "company_tel": '',
                "phone_number": '',
                "tel": '',
                "corp_ids": '',
                "status_arr": '',
                "data_type_arr": '',
                "category_arr": '',
                "not_corp_ids": '',
                "page_num": '',
                "page_size": '',
                "total_size": '',
                "account": '',
                "password": '',
                "fullname": '',
                "root_id": '',
                "parent_id": '',
                "department": '',
                "position": '',
                "interest_category": '',
                "auth_type": '',
                "auth_value": '',
                "payment_id": '',
                "login_count": '',
                "password_update": '',
                "app_token": '',
                "company_logo": '',
                "company_site": '',
                "bank_name": '',
                "account_name": '',
                "account_number": '',
                "seller_status": '',
                "seller_id": '',
                "reset_code": '',
                "coupon_code": '',
                "return_code": '',
                "device_type": '',
                "req_seq": '',
                "res_seq": '',
                "confirm_datetime": '',
                "withdraw_date": '',
                "occupation": '',
                "expired_date": '',
                "auto_login": '',
                "discount": '',
                "email_yn": '',
                "sms_yn": '',
                "ref_name": '',
                "ref_company_name": '',
                "tdi_token": '',
                "mk_token": '',
                "mk_s_id": '',
                "report_yn": '',
                "expired_start_date": '',
                "expired_end_date": '',
                "confirm_id": '',
                "corp_id": "CORP000036",
                "corp_cd": "17",
                "corp_nm": '',
                "corp_logo_img": "companyLogo/img-logo-kcb-s.png",
                "company_logo_file": '',
                "page_name": '',
                "corp_prof_inf": '',
                "corp_sup_data": '',
                "corp_sup_data_inf": '',
                "secsn_reason_cd": '',
                "secsn_reason_desc": '',
                "crt_dt": '',
                "crt_usr_id": '',
                "mdfy_dt": '',
                "mdfy_usr_id": '',
                "seq": '',
                "description": '',
                "product_cnt": '',
                "check_code": ''
            },
            {
                "product_id": '',
                "creator_user_id": '',
                "modified_user_id": '',
                "user_id": '',
                "contents_id": '',
                "seq_id": '',
                "status": '',
                "created_date": '',
                "modified_date": '',
                "search_type": '',
                "search_keyword": '',
                "company_name": "쿠콘",
                "type": '',
                "start_date": '',
                "end_date": '',
                "title": '',
                "hits": '',
                "price_type": '',
                "email": '',
                "level_cd": '',
                "gen": '',
                "sns_code": '',
                "ref_tel": '',
                "company_tel": '',
                "phone_number": '',
                "tel": '',
                "corp_ids": '',
                "status_arr": '',
                "data_type_arr": '',
                "category_arr": '',
                "not_corp_ids": '',
                "page_num": '',
                "page_size": '',
                "total_size": '',
                "account": '',
                "password": '',
                "fullname": '',
                "root_id": '',
                "parent_id": '',
                "department": '',
                "position": '',
                "interest_category": '',
                "auth_type": '',
                "auth_value": '',
                "payment_id": '',
                "login_count": '',
                "password_update": '',
                "app_token": '',
                "company_logo": '',
                "company_site": '',
                "bank_name": '',
                "account_name": '',
                "account_number": '',
                "seller_status": '',
                "seller_id": '',
                "reset_code": '',
                "coupon_code": '',
                "return_code": '',
                "device_type": '',
                "req_seq": '',
                "res_seq": '',
                "confirm_datetime": '',
                "withdraw_date": '',
                "occupation": '',
                "expired_date": '',
                "auto_login": '',
                "discount": '',
                "email_yn": '',
                "sms_yn": '',
                "ref_name": '',
                "ref_company_name": '',
                "tdi_token": '',
                "mk_token": '',
                "mk_s_id": '',
                "report_yn": '',
                "expired_start_date": '',
                "expired_end_date": '',
                "confirm_id": '',
                "corp_id": "CORP000020",
                "corp_cd": "44",
                "corp_nm": '',
                "corp_logo_img": "companyLogo/img-logo-coop-coocon.png",
                "company_logo_file": '',
                "page_name": '',
                "corp_prof_inf": '',
                "corp_sup_data": '',
                "corp_sup_data_inf": '',
                "secsn_reason_cd": '',
                "secsn_reason_desc": '',
                "crt_dt": '',
                "crt_usr_id": '',
                "mdfy_dt": '',
                "mdfy_usr_id": '',
                "seq": '',
                "description": '',
                "product_cnt": '',
                "check_code": ''
            }
        ]
    }

@app.get("/summary/list",tags=["summary"])
async def summary_list():
    return {
        "code": "200",
        "data": [
            {
                "product_id": '',
                "creator_user_id": '',
                "modified_user_id": '',
                "user_id": '',
                "contents_id": '',
                "seq_id": '',
                "status": '',
                "created_date": "2023-03-21 10:21:48.0",
                "modified_date": "2023-04-26 01:50:49.0",
                "search_type": '',
                "search_keyword": '',
                "company_name": '',
                "type": '',
                "start_date": '',
                "end_date": '',
                "title": '',
                "hits": "686",
                "price_type": '',
                "email": '',
                "level_cd": '',
                "gen": '',
                "sns_code": '',
                "ref_tel": '',
                "company_tel": '',
                "phone_number": '',
                "tel": '',
                "corp_ids": '',
                "status_arr": '',
                "data_type_arr": '',
                "category_arr": '',
                "not_corp_ids": '',
                "page_num": '',
                "page_size": '',
                "total_size": '',
                "pro_price_hist_id": '',
                "description": '',
                "category": '',
                "sale_start_date": '',
                "sale_end_date": '',
                "price": "350000",
                "my_price": '',
                "price_end": '',
                "provide_type": '',
                "data_type": '',
                "ref_id": '',
                "is_confirm": '',
                "thumbnail": "thumbnail/36572_1679643394395.jpg",
                "sample_type": "image",
                "sample": "sample/36572_1679643394445.jpg",
                "company_logo": "companyLogo/2023_03_16_110837_기본형.png",
                "root_id": '',
                "category_id": "CA000001",
                "corp_id": "CORP000047",
                "corp_logo": '',
                "legal_opinion_file": '',
                "keyword": '',
                "legal_opinion_filename": '',
                "structured_data_type": '',
                "file_type": '',
                "division_type": '',
                "start_data_term": '',
                "end_data_term": '',
                "category_array": '',
                "purchase_count": '',
                "interest_count": '',
                "is_enable": '',
                "user_name": '',
                "blog": '',
                "attachment_info": '',
                "licence": '',
                "url": '',
                "sort_type": '',
                "discount": '',
                "estimate_history_id": '',
                "link_type": '',
                "story_id": '',
                "board_type": '',
                "story_type": '',
                "data_code": '',
                "data_code_pre": '',
                "data_code_aft": '',
                "outlink_id": '',
                "grade": '',
                "download_count": '',
                "view_count": '',
                "popular_count": '',
                "is_cell": '',
                "product_group_id": '',
                "goods_size": '',
                "product_resource": '',
                "modi_type": '',
                "group_code": '',
                "img_type": '',
                "company_code": '',
                "code_name": '',
                "is_vs": '',
                "api_id": '',
                "extract_columns": '',
                "cart_type": '',
                "is_expired": '',
                "sorting_field": '',
                "sorting_type": '',
                "specs_id": "MA54230001",
                "popular_cnt": '',
                "specs_nm": "특허 서지사항 데이터",
                "category_name": "경제/산업",
                "product_cnt": "3",
                "corp_nm": "윕스",
                "recomend_prd_type_cd": '',
                "seq": '',
                "data_cd": '',
                "rtat_spd": '',
                "max_prd_price": '',
                "min_prd_price": '',
                "price_multiple": '',
                "price_type_opt1": '',
                "price_type_opt2": '',
                "price_type_opt3": '',
                "search_key": '',
                "prices": '',
                "categorys": '',
                "companys": '',
                "target_id": ''
            },
            {
                "product_id": '',
                "creator_user_id": '',
                "modified_user_id": '',
                "user_id": '',
                "contents_id": '',
                "seq_id": '',
                "status": '',
                "created_date": "2022-03-14 21:22:51.0",
                "modified_date": "2023-04-25 17:42:31.0",
                "search_type": '',
                "search_keyword": '',
                "company_name": '',
                "type": '',
                "start_date": '',
                "end_date": '',
                "title": '',
                "hits": "8359",
                "price_type": '',
                "email": '',
                "level_cd": '',
                "gen": '',
                "sns_code": '',
                "ref_tel": '',
                "company_tel": '',
                "phone_number": '',
                "tel": '',
                "corp_ids": '',
                "status_arr": '',
                "data_type_arr": '',
                "category_arr": '',
                "not_corp_ids": '',
                "page_num": '',
                "page_size": '',
                "total_size": '',
                "pro_price_hist_id": '',
                "description": '',
                "category": '',
                "sale_start_date": '',
                "sale_end_date": '',
                "price": "0",
                "my_price": '',
                "price_end": '',
                "provide_type": '',
                "data_type": '',
                "ref_id": '',
                "is_confirm": '',
                "thumbnail": "thumbnail/28839_1622012605748.jpg",
                "sample_type": "image",
                "sample": "sample/28839_1622012605750.jpg",
                "company_logo": "companyLogo/img-logo-gsretail-s.png",
                "root_id": '',
                "category_id": "CA000006",
                "corp_id": "CORP000032",
                "corp_logo": '',
                "legal_opinion_file": '',
                "keyword": '',
                "legal_opinion_filename": '',
                "structured_data_type": '',
                "file_type": '',
                "division_type": '',
                "start_data_term": '',
                "end_data_term": '',
                "category_array": '',
                "purchase_count": '',
                "interest_count": '',
                "is_enable": '',
                "user_name": '',
                "blog": '',
                "attachment_info": '',
                "licence": '',
                "url": '',
                "sort_type": '',
                "discount": '',
                "estimate_history_id": '',
                "link_type": '',
                "story_id": '',
                "board_type": '',
                "story_type": '',
                "data_code": '',
                "data_code_pre": '',
                "data_code_aft": '',
                "outlink_id": '',
                "grade": '',
                "download_count": '',
                "view_count": '',
                "popular_count": '',
                "is_cell": '',
                "product_group_id": '',
                "goods_size": '',
                "product_resource": '',
                "modi_type": '',
                "group_code": '',
                "img_type": '',
                "company_code": '',
                "code_name": '',
                "is_vs": '',
                "api_id": '',
                "extract_columns": '',
                "cart_type": '',
                "is_expired": '',
                "sorting_field": '',
                "sorting_type": '',
                "specs_id": "MA07190001",
                "popular_cnt": '',
                "specs_nm": "특성별 매출구성비",
                "category_name": "유통/마케팅",
                "product_cnt": "144",
                "corp_nm": "지에스리테일",
                "recomend_prd_type_cd": '',
                "seq": '',
                "data_cd": '',
                "rtat_spd": '',
                "max_prd_price": '',
                "min_prd_price": '',
                "price_multiple": '',
                "price_type_opt1": '',
                "price_type_opt2": '',
                "price_type_opt3": '',
                "search_key": '',
                "prices": '',
                "categorys": '',
                "companys": '',
                "target_id": ''
            },
            {
                "product_id": '',
                "creator_user_id": '',
                "modified_user_id": '',
                "user_id": '',
                "contents_id": '',
                "seq_id": '',
                "status": '',
                "created_date": "2022-03-14 21:22:51.0",
                "modified_date": "2023-04-25 17:42:21.0",
                "search_type": '',
                "search_keyword": '',
                "company_name": '',
                "type": '',
                "start_date": '',
                "end_date": '',
                "title": '',
                "hits": "1462",
                "price_type": '',
                "email": '',
                "level_cd": '',
                "gen": '',
                "sns_code": '',
                "ref_tel": '',
                "company_tel": '',
                "phone_number": '',
                "tel": '',
                "corp_ids": '',
                "status_arr": '',
                "data_type_arr": '',
                "category_arr": '',
                "not_corp_ids": '',
                "page_num": '',
                "page_size": '',
                "total_size": '',
                "pro_price_hist_id": '',
                "description": '',
                "category": '',
                "sale_start_date": '',
                "sale_end_date": '',
                "price": "0",
                "my_price": '',
                "price_end": '',
                "provide_type": '',
                "data_type": '',
                "ref_id": '',
                "is_confirm": '',
                "thumbnail": "thumbnail/28838_1622012494006.jpg",
                "sample_type": "image",
                "sample": "sample/28838_1622012494008.jpg",
                "company_logo": "companyLogo/img-logo-gsretail-s.png",
                "root_id": '',
                "category_id": "CA000006",
                "corp_id": "CORP000032",
                "corp_logo": '',
                "legal_opinion_file": '',
                "keyword": '',
                "legal_opinion_filename": '',
                "structured_data_type": '',
                "file_type": '',
                "division_type": '',
                "start_data_term": '',
                "end_data_term": '',
                "category_array": '',
                "purchase_count": '',
                "interest_count": '',
                "is_enable": '',
                "user_name": '',
                "blog": '',
                "attachment_info": '',
                "licence": '',
                "url": '',
                "sort_type": '',
                "discount": '',
                "estimate_history_id": '',
                "link_type": '',
                "story_id": '',
                "board_type": '',
                "story_type": '',
                "data_code": '',
                "data_code_pre": '',
                "data_code_aft": '',
                "outlink_id": '',
                "grade": '',
                "download_count": '',
                "view_count": '',
                "popular_count": '',
                "is_cell": '',
                "product_group_id": '',
                "goods_size": '',
                "product_resource": '',
                "modi_type": '',
                "group_code": '',
                "img_type": '',
                "company_code": '',
                "code_name": '',
                "is_vs": '',
                "api_id": '',
                "extract_columns": '',
                "cart_type": '',
                "is_expired": '',
                "sorting_field": '',
                "sorting_type": '',
                "specs_id": "MA07190002",
                "popular_cnt": '',
                "specs_nm": "고객구성비",
                "category_name": "유통/마케팅",
                "product_cnt": "27",
                "corp_nm": "지에스리테일",
                "recomend_prd_type_cd": '',
                "seq": '',
                "data_cd": '',
                "rtat_spd": '',
                "max_prd_price": '',
                "min_prd_price": '',
                "price_multiple": '',
                "price_type_opt1": '',
                "price_type_opt2": '',
                "price_type_opt3": '',
                "search_key": '',
                "prices": '',
                "categorys": '',
                "companys": '',
                "target_id": ''
            },
            {
                "product_id": '',
                "creator_user_id": '',
                "modified_user_id": '',
                "user_id": '',
                "contents_id": '',
                "seq_id": '',
                "status": '',
                "created_date": "2022-03-14 21:22:51.0",
                "modified_date": "2023-04-25 17:42:21.0",
                "search_type": '',
                "search_keyword": '',
                "company_name": '',
                "type": '',
                "start_date": '',
                "end_date": '',
                "title": '',
                "hits": "1350",
                "price_type": '',
                "email": '',
                "level_cd": '',
                "gen": '',
                "sns_code": '',
                "ref_tel": '',
                "company_tel": '',
                "phone_number": '',
                "tel": '',
                "corp_ids": '',
                "status_arr": '',
                "data_type_arr": '',
                "category_arr": '',
                "not_corp_ids": '',
                "page_num": '',
                "page_size": '',
                "total_size": '',
                "pro_price_hist_id": '',
                "description": '',
                "category": '',
                "sale_start_date": '',
                "sale_end_date": '',
                "price": "0",
                "my_price": '',
                "price_end": '',
                "provide_type": '',
                "data_type": '',
                "ref_id": '',
                "is_confirm": '',
                "thumbnail": "thumbnail/28837_1622012359965.jpg",
                "sample_type": "image",
                "sample": "sample/28837_1622012359968.jpg",
                "company_logo": "companyLogo/img-logo-gsretail-s.png",
                "root_id": '',
                "category_id": "CA000006",
                "corp_id": "CORP000032",
                "corp_logo": '',
                "legal_opinion_file": '',
                "keyword": '',
                "legal_opinion_filename": '',
                "structured_data_type": '',
                "file_type": '',
                "division_type": '',
                "start_data_term": '',
                "end_data_term": '',
                "category_array": '',
                "purchase_count": '',
                "interest_count": '',
                "is_enable": '',
                "user_name": '',
                "blog": '',
                "attachment_info": '',
                "licence": '',
                "url": '',
                "sort_type": '',
                "discount": '',
                "estimate_history_id": '',
                "link_type": '',
                "story_id": '',
                "board_type": '',
                "story_type": '',
                "data_code": '',
                "data_code_pre": '',
                "data_code_aft": '',
                "outlink_id": '',
                "grade": '',
                "download_count": '',
                "view_count": '',
                "popular_count": '',
                "is_cell": '',
                "product_group_id": '',
                "goods_size": '',
                "product_resource": '',
                "modi_type": '',
                "group_code": '',
                "img_type": '',
                "company_code": '',
                "code_name": '',
                "is_vs": '',
                "api_id": '',
                "extract_columns": '',
                "cart_type": '',
                "is_expired": '',
                "sorting_field": '',
                "sorting_type": '',
                "specs_id": "MA07190003",
                "popular_cnt": '',
                "specs_nm": "상품분류별 고객군별 평균구매횟수",
                "category_name": "유통/마케팅",
                "product_cnt": "14",
                "corp_nm": "지에스리테일",
                "recomend_prd_type_cd": '',
                "seq": '',
                "data_cd": '',
                "rtat_spd": '',
                "max_prd_price": '',
                "min_prd_price": '',
                "price_multiple": '',
                "price_type_opt1": '',
                "price_type_opt2": '',
                "price_type_opt3": '',
                "search_key": '',
                "prices": '',
                "categorys": '',
                "companys": '',
                "target_id": ''
            }
        ]
    }

@app.get("/data/101",tags=["101"])
async  def data_101():
    return [
        {
            "DL_YMW": "2022124",
            "DL_GD_SCLS_NM": "과일",
            "INVC_COUNT": "824429",
            "INVC_RANK": "1"
        },
        {
            "DL_YMW": "2022124",
            "DL_GD_SCLS_NM": "냉동/간편조리식품",
            "INVC_COUNT": "447478",
            "INVC_RANK": "2"
        },
        {
            "DL_YMW": "2022124",
            "DL_GD_SCLS_NM": "영양제",
            "INVC_COUNT": "418670",
            "INVC_RANK": "3"
        },
        {
            "DL_YMW": "2022124",
            "DL_GD_SCLS_NM": "생수",
            "INVC_COUNT": "308987",
            "INVC_RANK": "4"
        },
        {
            "DL_YMW": "2022124",
            "DL_GD_SCLS_NM": "채소",
            "INVC_COUNT": "275552",
            "INVC_RANK": "5"
        },
        {
            "DL_YMW": "2022124",
            "DL_GD_SCLS_NM": "빵류/떡류",
            "INVC_COUNT": "266511",
            "INVC_RANK": "6"
        },
        {
            "DL_YMW": "2022124",
            "DL_GD_SCLS_NM": "비타민제",
            "INVC_COUNT": "265145",
            "INVC_RANK": "7"
        },
        {
            "DL_YMW": "2022124",
            "DL_GD_SCLS_NM": "축산가공식품",
            "INVC_COUNT": "259455",
            "INVC_RANK": "8"
        },
        {
            "DL_YMW": "2022124",
            "DL_GD_SCLS_NM": "과자",
            "INVC_COUNT": "252416",
            "INVC_RANK": "9"
        },
        {
            "DL_YMW": "2022124",
            "DL_GD_SCLS_NM": "해산물/어패류",
            "INVC_COUNT": "221434",
            "INVC_RANK": "10"
        },
        {
            "DL_YMW": "2022124",
            "DL_GD_SCLS_NM": "기타건강식품",
            "INVC_COUNT": "207525",
            "INVC_RANK": "11"
        },
        {
            "DL_YMW": "2022124",
            "DL_GD_SCLS_NM": "커피",
            "INVC_COUNT": "207276",
            "INVC_RANK": "12"
        },
        {
            "DL_YMW": "2022124",
            "DL_GD_SCLS_NM": "다이어트식품",
            "INVC_COUNT": "193541",
            "INVC_RANK": "13"
        },
        {
            "DL_YMW": "2022124",
            "DL_GD_SCLS_NM": "차류",
            "INVC_COUNT": "161569",
            "INVC_RANK": "14"
        },
        {
            "DL_YMW": "2022124",
            "DL_GD_SCLS_NM": "탄산음료/탄산수",
            "INVC_COUNT": "155193",
            "INVC_RANK": "15"
        },
        {
            "DL_YMW": "2022124",
            "DL_GD_SCLS_NM": "쌀/잡곡",
            "INVC_COUNT": "145695",
            "INVC_RANK": "16"
        },
        {
            "DL_YMW": "2022124",
            "DL_GD_SCLS_NM": "기타식품",
            "INVC_COUNT": "141943",
            "INVC_RANK": "17"
        },
        {
            "DL_YMW": "2022124",
            "DL_GD_SCLS_NM": "생선",
            "INVC_COUNT": "138927",
            "INVC_RANK": "18"
        },
        {
            "DL_YMW": "2022124",
            "DL_GD_SCLS_NM": "유제품",
            "INVC_COUNT": "138084",
            "INVC_RANK": "19"
        },
        {
            "DL_YMW": "2022124",
            "DL_GD_SCLS_NM": "즉석밥",
            "INVC_COUNT": "134545",
            "INVC_RANK": "20"
        },
        {
            "DL_YMW": "2022124",
            "DL_GD_SCLS_NM": "조미료",
            "INVC_COUNT": "112395",
            "INVC_RANK": "21"
        },
        {
            "DL_YMW": "2022124",
            "DL_GD_SCLS_NM": "기타반찬류",
            "INVC_COUNT": "112254",
            "INVC_RANK": "22"
        },
        {
            "DL_YMW": "2022124",
            "DL_GD_SCLS_NM": "쇠고기",
            "INVC_COUNT": "108884",
            "INVC_RANK": "23"
        },
        {
            "DL_YMW": "2022124",
            "DL_GD_SCLS_NM": "만두/딤섬",
            "INVC_COUNT": "105677",
            "INVC_RANK": "24"
        },
        {
            "DL_YMW": "2022124",
            "DL_GD_SCLS_NM": "건어물",
            "INVC_COUNT": "102010",
            "INVC_RANK": "25"
        },
        {
            "DL_YMW": "2022124",
            "DL_GD_SCLS_NM": "견과류",
            "INVC_COUNT": "101481",
            "INVC_RANK": "26"
        },
        {
            "DL_YMW": "2022124",
            "DL_GD_SCLS_NM": "홍삼",
            "INVC_COUNT": "97313",
            "INVC_RANK": "27"
        },
        {
            "DL_YMW": "2022124",
            "DL_GD_SCLS_NM": "김/해초",
            "INVC_COUNT": "84675",
            "INVC_RANK": "28"
        },
        {
            "DL_YMW": "2022124",
            "DL_GD_SCLS_NM": "통조림",
            "INVC_COUNT": "79617",
            "INVC_RANK": "29"
        },
        {
            "DL_YMW": "2022124",
            "DL_GD_SCLS_NM": "라면",
            "INVC_COUNT": "73295",
            "INVC_RANK": "30"
        },
        {
            "DL_YMW": "2022123",
            "DL_GD_SCLS_NM": "과일",
            "INVC_COUNT": "736998",
            "INVC_RANK": "1"
        },
        {
            "DL_YMW": "2022123",
            "DL_GD_SCLS_NM": "냉동/간편조리식품",
            "INVC_COUNT": "443396",
            "INVC_RANK": "2"
        },
        {
            "DL_YMW": "2022123",
            "DL_GD_SCLS_NM": "영양제",
            "INVC_COUNT": "425747",
            "INVC_RANK": "3"
        },
        {
            "DL_YMW": "2022123",
            "DL_GD_SCLS_NM": "과자",
            "INVC_COUNT": "309069",
            "INVC_RANK": "4"
        },
        {
            "DL_YMW": "2022123",
            "DL_GD_SCLS_NM": "생수",
            "INVC_COUNT": "284233",
            "INVC_RANK": "5"
        },
        {
            "DL_YMW": "2022123",
            "DL_GD_SCLS_NM": "비타민제",
            "INVC_COUNT": "274397",
            "INVC_RANK": "6"
        },
        {
            "DL_YMW": "2022123",
            "DL_GD_SCLS_NM": "빵류/떡류",
            "INVC_COUNT": "270339",
            "INVC_RANK": "7"
        },
        {
            "DL_YMW": "2022123",
            "DL_GD_SCLS_NM": "축산가공식품",
            "INVC_COUNT": "257262",
            "INVC_RANK": "8"
        },
        {
            "DL_YMW": "2022123",
            "DL_GD_SCLS_NM": "채소",
            "INVC_COUNT": "245369",
            "INVC_RANK": "9"
        },
        {
            "DL_YMW": "2022123",
            "DL_GD_SCLS_NM": "커피",
            "INVC_COUNT": "220450",
            "INVC_RANK": "10"
        },
        {
            "DL_YMW": "2022123",
            "DL_GD_SCLS_NM": "해산물/어패류",
            "INVC_COUNT": "217619",
            "INVC_RANK": "11"
        },
        {
            "DL_YMW": "2022123",
            "DL_GD_SCLS_NM": "다이어트식품",
            "INVC_COUNT": "206445",
            "INVC_RANK": "12"
        },
        {
            "DL_YMW": "2022123",
            "DL_GD_SCLS_NM": "기타건강식품",
            "INVC_COUNT": "202934",
            "INVC_RANK": "13"
        },
        {
            "DL_YMW": "2022123",
            "DL_GD_SCLS_NM": "차류",
            "INVC_COUNT": "175790",
            "INVC_RANK": "14"
        },
        {
            "DL_YMW": "2022123",
            "DL_GD_SCLS_NM": "쌀/잡곡",
            "INVC_COUNT": "155882",
            "INVC_RANK": "15"
        },
        {
            "DL_YMW": "2022123",
            "DL_GD_SCLS_NM": "유제품",
            "INVC_COUNT": "153883",
            "INVC_RANK": "16"
        },
        {
            "DL_YMW": "2022123",
            "DL_GD_SCLS_NM": "탄산음료/탄산수",
            "INVC_COUNT": "153116",
            "INVC_RANK": "17"
        },
        {
            "DL_YMW": "2022123",
            "DL_GD_SCLS_NM": "기타식품",
            "INVC_COUNT": "145315",
            "INVC_RANK": "18"
        },
        {
            "DL_YMW": "2022123",
            "DL_GD_SCLS_NM": "즉석밥",
            "INVC_COUNT": "127561",
            "INVC_RANK": "19"
        },
        {
            "DL_YMW": "2022123",
            "DL_GD_SCLS_NM": "생선",
            "INVC_COUNT": "125359",
            "INVC_RANK": "20"
        },
        {
            "DL_YMW": "2022123",
            "DL_GD_SCLS_NM": "기타반찬류",
            "INVC_COUNT": "113575",
            "INVC_RANK": "21"
        },
        {
            "DL_YMW": "2022123",
            "DL_GD_SCLS_NM": "쇠고기",
            "INVC_COUNT": "107938",
            "INVC_RANK": "22"
        },
        {
            "DL_YMW": "2022123",
            "DL_GD_SCLS_NM": "견과류",
            "INVC_COUNT": "101790",
            "INVC_RANK": "23"
        },
        {
            "DL_YMW": "2022123",
            "DL_GD_SCLS_NM": "만두/딤섬",
            "INVC_COUNT": "101699",
            "INVC_RANK": "24"
        },
        {
            "DL_YMW": "2022123",
            "DL_GD_SCLS_NM": "건어물",
            "INVC_COUNT": "100992",
            "INVC_RANK": "25"
        },
        {
            "DL_YMW": "2022123",
            "DL_GD_SCLS_NM": "조미료",
            "INVC_COUNT": "88404",
            "INVC_RANK": "26"
        },
        {
            "DL_YMW": "2022123",
            "DL_GD_SCLS_NM": "홍삼",
            "INVC_COUNT": "80322",
            "INVC_RANK": "27"
        },
        {
            "DL_YMW": "2022123",
            "DL_GD_SCLS_NM": "김/해초",
            "INVC_COUNT": "79792",
            "INVC_RANK": "28"
        },
        {
            "DL_YMW": "2022123",
            "DL_GD_SCLS_NM": "라면",
            "INVC_COUNT": "75951",
            "INVC_RANK": "29"
        },
        {
            "DL_YMW": "2022123",
            "DL_GD_SCLS_NM": "두유",
            "INVC_COUNT": "74317",
            "INVC_RANK": "30"
        },
        {
            "DL_YMW": "2022122",
            "DL_GD_SCLS_NM": "과일",
            "INVC_COUNT": "785406",
            "INVC_RANK": "1"
        },
        {
            "DL_YMW": "2022122",
            "DL_GD_SCLS_NM": "영양제",
            "INVC_COUNT": "461118",
            "INVC_RANK": "2"
        },
        {
            "DL_YMW": "2022122",
            "DL_GD_SCLS_NM": "냉동/간편조리식품",
            "INVC_COUNT": "430758",
            "INVC_RANK": "3"
        },
        {
            "DL_YMW": "2022122",
            "DL_GD_SCLS_NM": "과자",
            "INVC_COUNT": "309494",
            "INVC_RANK": "4"
        },
        {
            "DL_YMW": "2022122",
            "DL_GD_SCLS_NM": "비타민제",
            "INVC_COUNT": "295128",
            "INVC_RANK": "5"
        },
        {
            "DL_YMW": "2022122",
            "DL_GD_SCLS_NM": "생수",
            "INVC_COUNT": "277331",
            "INVC_RANK": "6"
        },
        {
            "DL_YMW": "2022122",
            "DL_GD_SCLS_NM": "채소",
            "INVC_COUNT": "263830",
            "INVC_RANK": "7"
        },
        {
            "DL_YMW": "2022122",
            "DL_GD_SCLS_NM": "빵류/떡류",
            "INVC_COUNT": "244286",
            "INVC_RANK": "8"
        },
        {
            "DL_YMW": "2022122",
            "DL_GD_SCLS_NM": "축산가공식품",
            "INVC_COUNT": "229158",
            "INVC_RANK": "9"
        },
        {
            "DL_YMW": "2022122",
            "DL_GD_SCLS_NM": "커피",
            "INVC_COUNT": "224988",
            "INVC_RANK": "10"
        },
        {
            "DL_YMW": "2022122",
            "DL_GD_SCLS_NM": "다이어트식품",
            "INVC_COUNT": "211362",
            "INVC_RANK": "11"
        },
        {
            "DL_YMW": "2022122",
            "DL_GD_SCLS_NM": "해산물/어패류",
            "INVC_COUNT": "208586",
            "INVC_RANK": "12"
        },
        {
            "DL_YMW": "2022122",
            "DL_GD_SCLS_NM": "기타건강식품",
            "INVC_COUNT": "206560",
            "INVC_RANK": "13"
        },
        {
            "DL_YMW": "2022122",
            "DL_GD_SCLS_NM": "탄산음료/탄산수",
            "INVC_COUNT": "173856",
            "INVC_RANK": "14"
        },
        {
            "DL_YMW": "2022122",
            "DL_GD_SCLS_NM": "기타식품",
            "INVC_COUNT": "165837",
            "INVC_RANK": "15"
        },
        {
            "DL_YMW": "2022122",
            "DL_GD_SCLS_NM": "쌀/잡곡",
            "INVC_COUNT": "161124",
            "INVC_RANK": "16"
        },
        {
            "DL_YMW": "2022122",
            "DL_GD_SCLS_NM": "차류",
            "INVC_COUNT": "154631",
            "INVC_RANK": "17"
        },
        {
            "DL_YMW": "2022122",
            "DL_GD_SCLS_NM": "유제품",
            "INVC_COUNT": "146768",
            "INVC_RANK": "18"
        },
        {
            "DL_YMW": "2022122",
            "DL_GD_SCLS_NM": "즉석밥",
            "INVC_COUNT": "123618",
            "INVC_RANK": "19"
        },
        {
            "DL_YMW": "2022122",
            "DL_GD_SCLS_NM": "기타반찬류",
            "INVC_COUNT": "112769",
            "INVC_RANK": "20"
        },
        {
            "DL_YMW": "2022122",
            "DL_GD_SCLS_NM": "생선",
            "INVC_COUNT": "111354",
            "INVC_RANK": "21"
        },
        {
            "DL_YMW": "2022122",
            "DL_GD_SCLS_NM": "견과류",
            "INVC_COUNT": "108499",
            "INVC_RANK": "22"
        },
        {
            "DL_YMW": "2022122",
            "DL_GD_SCLS_NM": "건어물",
            "INVC_COUNT": "97474",
            "INVC_RANK": "23"
        },
        {
            "DL_YMW": "2022122",
            "DL_GD_SCLS_NM": "쇠고기",
            "INVC_COUNT": "91745",
            "INVC_RANK": "24"
        },
        {
            "DL_YMW": "2022122",
            "DL_GD_SCLS_NM": "조미료",
            "INVC_COUNT": "91623",
            "INVC_RANK": "25"
        },
        {
            "DL_YMW": "2022122",
            "DL_GD_SCLS_NM": "포기김치",
            "INVC_COUNT": "88865",
            "INVC_RANK": "26"
        },
        {
            "DL_YMW": "2022122",
            "DL_GD_SCLS_NM": "만두/딤섬",
            "INVC_COUNT": "82043",
            "INVC_RANK": "27"
        },
        {
            "DL_YMW": "2022122",
            "DL_GD_SCLS_NM": "두유",
            "INVC_COUNT": "81652",
            "INVC_RANK": "28"
        },
        {
            "DL_YMW": "2022122",
            "DL_GD_SCLS_NM": "김/해초",
            "INVC_COUNT": "81487",
            "INVC_RANK": "29"
        },
        {
            "DL_YMW": "2022122",
            "DL_GD_SCLS_NM": "홍삼",
            "INVC_COUNT": "77946",
            "INVC_RANK": "30"
        },
        {
            "DL_YMW": "2022121",
            "DL_GD_SCLS_NM": "과일",
            "INVC_COUNT": "843357",
            "INVC_RANK": "1"
        },
        {
            "DL_YMW": "2022121",
            "DL_GD_SCLS_NM": "냉동/간편조리식품",
            "INVC_COUNT": "447767",
            "INVC_RANK": "2"
        },
        {
            "DL_YMW": "2022121",
            "DL_GD_SCLS_NM": "영양제",
            "INVC_COUNT": "430092",
            "INVC_RANK": "3"
        },
        {
            "DL_YMW": "2022121",
            "DL_GD_SCLS_NM": "생수",
            "INVC_COUNT": "307104",
            "INVC_RANK": "4"
        },
        {
            "DL_YMW": "2022121",
            "DL_GD_SCLS_NM": "과자",
            "INVC_COUNT": "273507",
            "INVC_RANK": "5"
        },
        {
            "DL_YMW": "2022121",
            "DL_GD_SCLS_NM": "커피",
            "INVC_COUNT": "255719",
            "INVC_RANK": "6"
        },
        {
            "DL_YMW": "2022121",
            "DL_GD_SCLS_NM": "채소",
            "INVC_COUNT": "239081",
            "INVC_RANK": "7"
        },
        {
            "DL_YMW": "2022121",
            "DL_GD_SCLS_NM": "다이어트식품",
            "INVC_COUNT": "198925",
            "INVC_RANK": "8"
        },
        {
            "DL_YMW": "2022121",
            "DL_GD_SCLS_NM": "쌀/잡곡",
            "INVC_COUNT": "197872",
            "INVC_RANK": "9"
        },
        {
            "DL_YMW": "2022121",
            "DL_GD_SCLS_NM": "빵류/떡류",
            "INVC_COUNT": "195870",
            "INVC_RANK": "10"
        },
        {
            "DL_YMW": "2022121",
            "DL_GD_SCLS_NM": "기타건강식품",
            "INVC_COUNT": "192825",
            "INVC_RANK": "11"
        },
        {
            "DL_YMW": "2022121",
            "DL_GD_SCLS_NM": "축산가공식품",
            "INVC_COUNT": "190416",
            "INVC_RANK": "12"
        },
        {
            "DL_YMW": "2022121",
            "DL_GD_SCLS_NM": "기타식품",
            "INVC_COUNT": "176004",
            "INVC_RANK": "13"
        },
        {
            "DL_YMW": "2022121",
            "DL_GD_SCLS_NM": "유제품",
            "INVC_COUNT": "174632",
            "INVC_RANK": "14"
        },
        {
            "DL_YMW": "2022121",
            "DL_GD_SCLS_NM": "비타민제",
            "INVC_COUNT": "171168",
            "INVC_RANK": "15"
        },
        {
            "DL_YMW": "2022121",
            "DL_GD_SCLS_NM": "차류",
            "INVC_COUNT": "144565",
            "INVC_RANK": "16"
        },
        {
            "DL_YMW": "2022121",
            "DL_GD_SCLS_NM": "해산물/어패류",
            "INVC_COUNT": "134530",
            "INVC_RANK": "17"
        },
        {
            "DL_YMW": "2022121",
            "DL_GD_SCLS_NM": "탄산음료/탄산수",
            "INVC_COUNT": "131309",
            "INVC_RANK": "18"
        },
        {
            "DL_YMW": "2022121",
            "DL_GD_SCLS_NM": "만두/딤섬",
            "INVC_COUNT": "116277",
            "INVC_RANK": "19"
        },
        {
            "DL_YMW": "2022121",
            "DL_GD_SCLS_NM": "즉석밥",
            "INVC_COUNT": "107708",
            "INVC_RANK": "20"
        },
        {
            "DL_YMW": "2022121",
            "DL_GD_SCLS_NM": "견과류",
            "INVC_COUNT": "97719",
            "INVC_RANK": "21"
        },
        {
            "DL_YMW": "2022121",
            "DL_GD_SCLS_NM": "생선",
            "INVC_COUNT": "96780",
            "INVC_RANK": "22"
        },
        {
            "DL_YMW": "2022121",
            "DL_GD_SCLS_NM": "김/해초",
            "INVC_COUNT": "86683",
            "INVC_RANK": "23"
        },
        {
            "DL_YMW": "2022121",
            "DL_GD_SCLS_NM": "조미료",
            "INVC_COUNT": "85702",
            "INVC_RANK": "24"
        },
        {
            "DL_YMW": "2022121",
            "DL_GD_SCLS_NM": "건어물",
            "INVC_COUNT": "80019",
            "INVC_RANK": "25"
        },
        {
            "DL_YMW": "2022121",
            "DL_GD_SCLS_NM": "포기김치",
            "INVC_COUNT": "77167",
            "INVC_RANK": "26"
        },
        {
            "DL_YMW": "2022121",
            "DL_GD_SCLS_NM": "쇠고기",
            "INVC_COUNT": "73872",
            "INVC_RANK": "27"
        },
        {
            "DL_YMW": "2022121",
            "DL_GD_SCLS_NM": "기타농산물",
            "INVC_COUNT": "70745",
            "INVC_RANK": "28"
        },
        {
            "DL_YMW": "2022121",
            "DL_GD_SCLS_NM": "두유",
            "INVC_COUNT": "70625",
            "INVC_RANK": "29"
        },
        {
            "DL_YMW": "2022121",
            "DL_GD_SCLS_NM": "홍삼",
            "INVC_COUNT": "65693",
            "INVC_RANK": "30"
        },
        {
            "DL_YMW": "2022115",
            "DL_GD_SCLS_NM": "과일",
            "INVC_COUNT": "776594",
            "INVC_RANK": "1"
        },
        {
            "DL_YMW": "2022115",
            "DL_GD_SCLS_NM": "영양제",
            "INVC_COUNT": "451790",
            "INVC_RANK": "2"
        },
        {
            "DL_YMW": "2022115",
            "DL_GD_SCLS_NM": "냉동/간편조리식품",
            "INVC_COUNT": "434203",
            "INVC_RANK": "3"
        },
        {
            "DL_YMW": "2022115",
            "DL_GD_SCLS_NM": "생수",
            "INVC_COUNT": "343552",
            "INVC_RANK": "4"
        },
        {
            "DL_YMW": "2022115",
            "DL_GD_SCLS_NM": "커피",
            "INVC_COUNT": "262069",
            "INVC_RANK": "5"
        },
        {
            "DL_YMW": "2022115",
            "DL_GD_SCLS_NM": "과자",
            "INVC_COUNT": "258578",
            "INVC_RANK": "6"
        },
        {
            "DL_YMW": "2022115",
            "DL_GD_SCLS_NM": "채소",
            "INVC_COUNT": "238061",
            "INVC_RANK": "7"
        },
        {
            "DL_YMW": "2022115",
            "DL_GD_SCLS_NM": "빵류/떡류",
            "INVC_COUNT": "232173",
            "INVC_RANK": "8"
        },
        {
            "DL_YMW": "2022115",
            "DL_GD_SCLS_NM": "축산가공식품",
            "INVC_COUNT": "213765",
            "INVC_RANK": "9"
        },
        {
            "DL_YMW": "2022115",
            "DL_GD_SCLS_NM": "다이어트식품",
            "INVC_COUNT": "203176",
            "INVC_RANK": "10"
        },
        {
            "DL_YMW": "2022115",
            "DL_GD_SCLS_NM": "쌀/잡곡",
            "INVC_COUNT": "197668",
            "INVC_RANK": "11"
        },
        {
            "DL_YMW": "2022115",
            "DL_GD_SCLS_NM": "기타건강식품",
            "INVC_COUNT": "185017",
            "INVC_RANK": "12"
        },
        {
            "DL_YMW": "2022115",
            "DL_GD_SCLS_NM": "기타식품",
            "INVC_COUNT": "183551",
            "INVC_RANK": "13"
        },
        {
            "DL_YMW": "2022115",
            "DL_GD_SCLS_NM": "비타민제",
            "INVC_COUNT": "173991",
            "INVC_RANK": "14"
        },
        {
            "DL_YMW": "2022115",
            "DL_GD_SCLS_NM": "유제품",
            "INVC_COUNT": "168019",
            "INVC_RANK": "15"
        },
        {
            "DL_YMW": "2022115",
            "DL_GD_SCLS_NM": "탄산음료/탄산수",
            "INVC_COUNT": "167270",
            "INVC_RANK": "16"
        },
        {
            "DL_YMW": "2022115",
            "DL_GD_SCLS_NM": "해산물/어패류",
            "INVC_COUNT": "146600",
            "INVC_RANK": "17"
        },
        {
            "DL_YMW": "2022115",
            "DL_GD_SCLS_NM": "차류",
            "INVC_COUNT": "135994",
            "INVC_RANK": "18"
        },
        {
            "DL_YMW": "2022115",
            "DL_GD_SCLS_NM": "즉석밥",
            "INVC_COUNT": "117178",
            "INVC_RANK": "19"
        },
        {
            "DL_YMW": "2022115",
            "DL_GD_SCLS_NM": "만두/딤섬",
            "INVC_COUNT": "114289",
            "INVC_RANK": "20"
        },
        {
            "DL_YMW": "2022115",
            "DL_GD_SCLS_NM": "절임배추",
            "INVC_COUNT": "111297",
            "INVC_RANK": "21"
        },
        {
            "DL_YMW": "2022115",
            "DL_GD_SCLS_NM": "견과류",
            "INVC_COUNT": "106330",
            "INVC_RANK": "22"
        },
        {
            "DL_YMW": "2022115",
            "DL_GD_SCLS_NM": "생선",
            "INVC_COUNT": "93035",
            "INVC_RANK": "23"
        },
        {
            "DL_YMW": "2022115",
            "DL_GD_SCLS_NM": "포기김치",
            "INVC_COUNT": "91994",
            "INVC_RANK": "24"
        },
        {
            "DL_YMW": "2022115",
            "DL_GD_SCLS_NM": "조미료",
            "INVC_COUNT": "89550",
            "INVC_RANK": "25"
        },
        {
            "DL_YMW": "2022115",
            "DL_GD_SCLS_NM": "건어물",
            "INVC_COUNT": "84213",
            "INVC_RANK": "26"
        },
        {
            "DL_YMW": "2022115",
            "DL_GD_SCLS_NM": "쇠고기",
            "INVC_COUNT": "75267",
            "INVC_RANK": "27"
        },
        {
            "DL_YMW": "2022115",
            "DL_GD_SCLS_NM": "통조림",
            "INVC_COUNT": "72124",
            "INVC_RANK": "28"
        },
        {
            "DL_YMW": "2022115",
            "DL_GD_SCLS_NM": "김/해초",
            "INVC_COUNT": "70770",
            "INVC_RANK": "29"
        },
        {
            "DL_YMW": "2022115",
            "DL_GD_SCLS_NM": "라면",
            "INVC_COUNT": "68618",
            "INVC_RANK": "30"
        },
        {
            "DL_YMW": "2022114",
            "DL_GD_SCLS_NM": "과일",
            "INVC_COUNT": "750761",
            "INVC_RANK": "1"
        },
        {
            "DL_YMW": "2022114",
            "DL_GD_SCLS_NM": "영양제",
            "INVC_COUNT": "425947",
            "INVC_RANK": "2"
        },
        {
            "DL_YMW": "2022114",
            "DL_GD_SCLS_NM": "생수",
            "INVC_COUNT": "410080",
            "INVC_RANK": "3"
        },
        {
            "DL_YMW": "2022114",
            "DL_GD_SCLS_NM": "냉동/간편조리식품",
            "INVC_COUNT": "396472",
            "INVC_RANK": "4"
        },
        {
            "DL_YMW": "2022114",
            "DL_GD_SCLS_NM": "과자",
            "INVC_COUNT": "269271",
            "INVC_RANK": "5"
        },
        {
            "DL_YMW": "2022114",
            "DL_GD_SCLS_NM": "커피",
            "INVC_COUNT": "249885",
            "INVC_RANK": "6"
        },
        {
            "DL_YMW": "2022114",
            "DL_GD_SCLS_NM": "다이어트식품",
            "INVC_COUNT": "204383",
            "INVC_RANK": "7"
        },
        {
            "DL_YMW": "2022114",
            "DL_GD_SCLS_NM": "채소",
            "INVC_COUNT": "201451",
            "INVC_RANK": "8"
        },
        {
            "DL_YMW": "2022114",
            "DL_GD_SCLS_NM": "기타건강식품",
            "INVC_COUNT": "190497",
            "INVC_RANK": "9"
        },
        {
            "DL_YMW": "2022114",
            "DL_GD_SCLS_NM": "축산가공식품",
            "INVC_COUNT": "189734",
            "INVC_RANK": "10"
        },
        {
            "DL_YMW": "2022114",
            "DL_GD_SCLS_NM": "쌀/잡곡",
            "INVC_COUNT": "185769",
            "INVC_RANK": "11"
        },
        {
            "DL_YMW": "2022114",
            "DL_GD_SCLS_NM": "기타식품",
            "INVC_COUNT": "181452",
            "INVC_RANK": "12"
        },
        {
            "DL_YMW": "2022114",
            "DL_GD_SCLS_NM": "빵류/떡류",
            "INVC_COUNT": "176718",
            "INVC_RANK": "13"
        },
        {
            "DL_YMW": "2022114",
            "DL_GD_SCLS_NM": "비타민제",
            "INVC_COUNT": "170212",
            "INVC_RANK": "14"
        },
        {
            "DL_YMW": "2022114",
            "DL_GD_SCLS_NM": "유제품",
            "INVC_COUNT": "164438",
            "INVC_RANK": "15"
        },
        {
            "DL_YMW": "2022114",
            "DL_GD_SCLS_NM": "해산물/어패류",
            "INVC_COUNT": "161588",
            "INVC_RANK": "16"
        },
        {
            "DL_YMW": "2022114",
            "DL_GD_SCLS_NM": "절임배추",
            "INVC_COUNT": "154720",
            "INVC_RANK": "17"
        },
        {
            "DL_YMW": "2022114",
            "DL_GD_SCLS_NM": "탄산음료/탄산수",
            "INVC_COUNT": "130520",
            "INVC_RANK": "18"
        },
        {
            "DL_YMW": "2022114",
            "DL_GD_SCLS_NM": "차류",
            "INVC_COUNT": "129389",
            "INVC_RANK": "19"
        },
        {
            "DL_YMW": "2022114",
            "DL_GD_SCLS_NM": "견과류",
            "INVC_COUNT": "107304",
            "INVC_RANK": "20"
        },
        {
            "DL_YMW": "2022114",
            "DL_GD_SCLS_NM": "포기김치",
            "INVC_COUNT": "105929",
            "INVC_RANK": "21"
        },
        {
            "DL_YMW": "2022114",
            "DL_GD_SCLS_NM": "즉석밥",
            "INVC_COUNT": "95921",
            "INVC_RANK": "22"
        },
        {
            "DL_YMW": "2022114",
            "DL_GD_SCLS_NM": "생선",
            "INVC_COUNT": "94043",
            "INVC_RANK": "23"
        },
        {
            "DL_YMW": "2022114",
            "DL_GD_SCLS_NM": "만두/딤섬",
            "INVC_COUNT": "91243",
            "INVC_RANK": "24"
        },
        {
            "DL_YMW": "2022114",
            "DL_GD_SCLS_NM": "건어물",
            "INVC_COUNT": "88691",
            "INVC_RANK": "25"
        },
        {
            "DL_YMW": "2022114",
            "DL_GD_SCLS_NM": "조미료",
            "INVC_COUNT": "88562",
            "INVC_RANK": "26"
        },
        {
            "DL_YMW": "2022114",
            "DL_GD_SCLS_NM": "두유",
            "INVC_COUNT": "72543",
            "INVC_RANK": "27"
        },
        {
            "DL_YMW": "2022114",
            "DL_GD_SCLS_NM": "김/해초",
            "INVC_COUNT": "66671",
            "INVC_RANK": "28"
        },
        {
            "DL_YMW": "2022114",
            "DL_GD_SCLS_NM": "기타농산물",
            "INVC_COUNT": "64966",
            "INVC_RANK": "29"
        },
        {
            "DL_YMW": "2022114",
            "DL_GD_SCLS_NM": "홍삼",
            "INVC_COUNT": "57937",
            "INVC_RANK": "30"
        },
        {
            "DL_YMW": "2022113",
            "DL_GD_SCLS_NM": "과일",
            "INVC_COUNT": "724855",
            "INVC_RANK": "1"
        },
        {
            "DL_YMW": "2022113",
            "DL_GD_SCLS_NM": "과자",
            "INVC_COUNT": "468666",
            "INVC_RANK": "2"
        },
        {
            "DL_YMW": "2022113",
            "DL_GD_SCLS_NM": "영양제",
            "INVC_COUNT": "458306",
            "INVC_RANK": "3"
        },
        {
            "DL_YMW": "2022113",
            "DL_GD_SCLS_NM": "냉동/간편조리식품",
            "INVC_COUNT": "392455",
            "INVC_RANK": "4"
        },
        {
            "DL_YMW": "2022113",
            "DL_GD_SCLS_NM": "생수",
            "INVC_COUNT": "351479",
            "INVC_RANK": "5"
        },
        {
            "DL_YMW": "2022113",
            "DL_GD_SCLS_NM": "커피",
            "INVC_COUNT": "239355",
            "INVC_RANK": "6"
        },
        {
            "DL_YMW": "2022113",
            "DL_GD_SCLS_NM": "채소",
            "INVC_COUNT": "211698",
            "INVC_RANK": "7"
        },
        {
            "DL_YMW": "2022113",
            "DL_GD_SCLS_NM": "다이어트식품",
            "INVC_COUNT": "211622",
            "INVC_RANK": "8"
        },
        {
            "DL_YMW": "2022113",
            "DL_GD_SCLS_NM": "축산가공식품",
            "INVC_COUNT": "204744",
            "INVC_RANK": "9"
        },
        {
            "DL_YMW": "2022113",
            "DL_GD_SCLS_NM": "빵류/떡류",
            "INVC_COUNT": "203315",
            "INVC_RANK": "10"
        },
        {
            "DL_YMW": "2022113",
            "DL_GD_SCLS_NM": "기타식품",
            "INVC_COUNT": "200962",
            "INVC_RANK": "11"
        },
        {
            "DL_YMW": "2022113",
            "DL_GD_SCLS_NM": "쌀/잡곡",
            "INVC_COUNT": "198413",
            "INVC_RANK": "12"
        },
        {
            "DL_YMW": "2022113",
            "DL_GD_SCLS_NM": "기타건강식품",
            "INVC_COUNT": "189318",
            "INVC_RANK": "13"
        },
        {
            "DL_YMW": "2022113",
            "DL_GD_SCLS_NM": "유제품",
            "INVC_COUNT": "181438",
            "INVC_RANK": "14"
        },
        {
            "DL_YMW": "2022113",
            "DL_GD_SCLS_NM": "비타민제",
            "INVC_COUNT": "179271",
            "INVC_RANK": "15"
        },
        {
            "DL_YMW": "2022113",
            "DL_GD_SCLS_NM": "탄산음료/탄산수",
            "INVC_COUNT": "169586",
            "INVC_RANK": "16"
        },
        {
            "DL_YMW": "2022113",
            "DL_GD_SCLS_NM": "해산물/어패류",
            "INVC_COUNT": "152547",
            "INVC_RANK": "17"
        },
        {
            "DL_YMW": "2022113",
            "DL_GD_SCLS_NM": "차류",
            "INVC_COUNT": "137431",
            "INVC_RANK": "18"
        },
        {
            "DL_YMW": "2022113",
            "DL_GD_SCLS_NM": "즉석밥",
            "INVC_COUNT": "117949",
            "INVC_RANK": "19"
        },
        {
            "DL_YMW": "2022113",
            "DL_GD_SCLS_NM": "절임배추",
            "INVC_COUNT": "115869",
            "INVC_RANK": "20"
        },
        {
            "DL_YMW": "2022113",
            "DL_GD_SCLS_NM": "포기김치",
            "INVC_COUNT": "114875",
            "INVC_RANK": "21"
        },
        {
            "DL_YMW": "2022113",
            "DL_GD_SCLS_NM": "견과류",
            "INVC_COUNT": "102261",
            "INVC_RANK": "22"
        },
        {
            "DL_YMW": "2022113",
            "DL_GD_SCLS_NM": "조미료",
            "INVC_COUNT": "93457",
            "INVC_RANK": "23"
        },
        {
            "DL_YMW": "2022113",
            "DL_GD_SCLS_NM": "생선",
            "INVC_COUNT": "91839",
            "INVC_RANK": "24"
        },
        {
            "DL_YMW": "2022113",
            "DL_GD_SCLS_NM": "만두/딤섬",
            "INVC_COUNT": "83815",
            "INVC_RANK": "25"
        },
        {
            "DL_YMW": "2022113",
            "DL_GD_SCLS_NM": "두유",
            "INVC_COUNT": "82766",
            "INVC_RANK": "26"
        },
        {
            "DL_YMW": "2022113",
            "DL_GD_SCLS_NM": "기타농산물",
            "INVC_COUNT": "75583",
            "INVC_RANK": "27"
        },
        {
            "DL_YMW": "2022113",
            "DL_GD_SCLS_NM": "건어물",
            "INVC_COUNT": "74936",
            "INVC_RANK": "28"
        },
        {
            "DL_YMW": "2022113",
            "DL_GD_SCLS_NM": "김/해초",
            "INVC_COUNT": "66453",
            "INVC_RANK": "29"
        },
        {
            "DL_YMW": "2022113",
            "DL_GD_SCLS_NM": "통조림",
            "INVC_COUNT": "63785",
            "INVC_RANK": "30"
        },
        {
            "DL_YMW": "2022112",
            "DL_GD_SCLS_NM": "과일",
            "INVC_COUNT": "731522",
            "INVC_RANK": "1"
        },
        {
            "DL_YMW": "2022112",
            "DL_GD_SCLS_NM": "생수",
            "INVC_COUNT": "515286",
            "INVC_RANK": "2"
        },
        {
            "DL_YMW": "2022112",
            "DL_GD_SCLS_NM": "영양제",
            "INVC_COUNT": "508331",
            "INVC_RANK": "3"
        },
        {
            "DL_YMW": "2022112",
            "DL_GD_SCLS_NM": "과자",
            "INVC_COUNT": "439938",
            "INVC_RANK": "4"
        },
        {
            "DL_YMW": "2022112",
            "DL_GD_SCLS_NM": "냉동/간편조리식품",
            "INVC_COUNT": "424835",
            "INVC_RANK": "5"
        },
        {
            "DL_YMW": "2022112",
            "DL_GD_SCLS_NM": "커피",
            "INVC_COUNT": "295584",
            "INVC_RANK": "6"
        },
        {
            "DL_YMW": "2022112",
            "DL_GD_SCLS_NM": "다이어트식품",
            "INVC_COUNT": "242638",
            "INVC_RANK": "7"
        },
        {
            "DL_YMW": "2022112",
            "DL_GD_SCLS_NM": "쌀/잡곡",
            "INVC_COUNT": "238910",
            "INVC_RANK": "8"
        },
        {
            "DL_YMW": "2022112",
            "DL_GD_SCLS_NM": "채소",
            "INVC_COUNT": "223745",
            "INVC_RANK": "9"
        },
        {
            "DL_YMW": "2022112",
            "DL_GD_SCLS_NM": "기타건강식품",
            "INVC_COUNT": "215906",
            "INVC_RANK": "10"
        },
        {
            "DL_YMW": "2022112",
            "DL_GD_SCLS_NM": "축산가공식품",
            "INVC_COUNT": "205524",
            "INVC_RANK": "11"
        },
        {
            "DL_YMW": "2022112",
            "DL_GD_SCLS_NM": "빵류/떡류",
            "INVC_COUNT": "196836",
            "INVC_RANK": "12"
        },
        {
            "DL_YMW": "2022112",
            "DL_GD_SCLS_NM": "비타민제",
            "INVC_COUNT": "194324",
            "INVC_RANK": "13"
        },
        {
            "DL_YMW": "2022112",
            "DL_GD_SCLS_NM": "유제품",
            "INVC_COUNT": "184479",
            "INVC_RANK": "14"
        },
        {
            "DL_YMW": "2022112",
            "DL_GD_SCLS_NM": "해산물/어패류",
            "INVC_COUNT": "175868",
            "INVC_RANK": "15"
        },
        {
            "DL_YMW": "2022112",
            "DL_GD_SCLS_NM": "기타식품",
            "INVC_COUNT": "171493",
            "INVC_RANK": "16"
        },
        {
            "DL_YMW": "2022112",
            "DL_GD_SCLS_NM": "탄산음료/탄산수",
            "INVC_COUNT": "160093",
            "INVC_RANK": "17"
        },
        {
            "DL_YMW": "2022112",
            "DL_GD_SCLS_NM": "차류",
            "INVC_COUNT": "148672",
            "INVC_RANK": "18"
        },
        {
            "DL_YMW": "2022112",
            "DL_GD_SCLS_NM": "포기김치",
            "INVC_COUNT": "137620",
            "INVC_RANK": "19"
        },
        {
            "DL_YMW": "2022112",
            "DL_GD_SCLS_NM": "만두/딤섬",
            "INVC_COUNT": "134109",
            "INVC_RANK": "20"
        },
        {
            "DL_YMW": "2022112",
            "DL_GD_SCLS_NM": "견과류",
            "INVC_COUNT": "130029",
            "INVC_RANK": "21"
        },
        {
            "DL_YMW": "2022112",
            "DL_GD_SCLS_NM": "즉석밥",
            "INVC_COUNT": "110463",
            "INVC_RANK": "22"
        },
        {
            "DL_YMW": "2022112",
            "DL_GD_SCLS_NM": "조미료",
            "INVC_COUNT": "108623",
            "INVC_RANK": "23"
        },
        {
            "DL_YMW": "2022112",
            "DL_GD_SCLS_NM": "생선",
            "INVC_COUNT": "106019",
            "INVC_RANK": "24"
        },
        {
            "DL_YMW": "2022112",
            "DL_GD_SCLS_NM": "건어물",
            "INVC_COUNT": "88789",
            "INVC_RANK": "25"
        },
        {
            "DL_YMW": "2022112",
            "DL_GD_SCLS_NM": "기타농산물",
            "INVC_COUNT": "84492",
            "INVC_RANK": "26"
        },
        {
            "DL_YMW": "2022112",
            "DL_GD_SCLS_NM": "김/해초",
            "INVC_COUNT": "80040",
            "INVC_RANK": "27"
        },
        {
            "DL_YMW": "2022112",
            "DL_GD_SCLS_NM": "두유",
            "INVC_COUNT": "76925",
            "INVC_RANK": "28"
        },
        {
            "DL_YMW": "2022112",
            "DL_GD_SCLS_NM": "쇠고기",
            "INVC_COUNT": "69393",
            "INVC_RANK": "29"
        },
        {
            "DL_YMW": "2022112",
            "DL_GD_SCLS_NM": "면류",
            "INVC_COUNT": "65748",
            "INVC_RANK": "30"
        },
        {
            "DL_YMW": "2022111",
            "DL_GD_SCLS_NM": "과일",
            "INVC_COUNT": "706023",
            "INVC_RANK": "1"
        },
        {
            "DL_YMW": "2022111",
            "DL_GD_SCLS_NM": "영양제",
            "INVC_COUNT": "501838",
            "INVC_RANK": "2"
        },
        {
            "DL_YMW": "2022111",
            "DL_GD_SCLS_NM": "생수",
            "INVC_COUNT": "495207",
            "INVC_RANK": "3"
        },
        {
            "DL_YMW": "2022111",
            "DL_GD_SCLS_NM": "냉동/간편조리식품",
            "INVC_COUNT": "432009",
            "INVC_RANK": "4"
        },
        {
            "DL_YMW": "2022111",
            "DL_GD_SCLS_NM": "과자",
            "INVC_COUNT": "333769",
            "INVC_RANK": "5"
        },
        {
            "DL_YMW": "2022111",
            "DL_GD_SCLS_NM": "커피",
            "INVC_COUNT": "278847",
            "INVC_RANK": "6"
        },
        {
            "DL_YMW": "2022111",
            "DL_GD_SCLS_NM": "쌀/잡곡",
            "INVC_COUNT": "237382",
            "INVC_RANK": "7"
        },
        {
            "DL_YMW": "2022111",
            "DL_GD_SCLS_NM": "채소",
            "INVC_COUNT": "216681",
            "INVC_RANK": "8"
        },
        {
            "DL_YMW": "2022111",
            "DL_GD_SCLS_NM": "다이어트식품",
            "INVC_COUNT": "213403",
            "INVC_RANK": "9"
        },
        {
            "DL_YMW": "2022111",
            "DL_GD_SCLS_NM": "기타건강식품",
            "INVC_COUNT": "212425",
            "INVC_RANK": "10"
        },
        {
            "DL_YMW": "2022111",
            "DL_GD_SCLS_NM": "축산가공식품",
            "INVC_COUNT": "201360",
            "INVC_RANK": "11"
        },
        {
            "DL_YMW": "2022111",
            "DL_GD_SCLS_NM": "빵류/떡류",
            "INVC_COUNT": "185785",
            "INVC_RANK": "12"
        },
        {
            "DL_YMW": "2022111",
            "DL_GD_SCLS_NM": "비타민제",
            "INVC_COUNT": "180586",
            "INVC_RANK": "13"
        },
        {
            "DL_YMW": "2022111",
            "DL_GD_SCLS_NM": "유제품",
            "INVC_COUNT": "175424",
            "INVC_RANK": "14"
        },
        {
            "DL_YMW": "2022111",
            "DL_GD_SCLS_NM": "기타식품",
            "INVC_COUNT": "169368",
            "INVC_RANK": "15"
        },
        {
            "DL_YMW": "2022111",
            "DL_GD_SCLS_NM": "해산물/어패류",
            "INVC_COUNT": "164228",
            "INVC_RANK": "16"
        },
        {
            "DL_YMW": "2022111",
            "DL_GD_SCLS_NM": "탄산음료/탄산수",
            "INVC_COUNT": "144896",
            "INVC_RANK": "17"
        },
        {
            "DL_YMW": "2022111",
            "DL_GD_SCLS_NM": "차류",
            "INVC_COUNT": "128730",
            "INVC_RANK": "18"
        },
        {
            "DL_YMW": "2022111",
            "DL_GD_SCLS_NM": "포기김치",
            "INVC_COUNT": "122767",
            "INVC_RANK": "19"
        },
        {
            "DL_YMW": "2022111",
            "DL_GD_SCLS_NM": "즉석밥",
            "INVC_COUNT": "122610",
            "INVC_RANK": "20"
        },
        {
            "DL_YMW": "2022111",
            "DL_GD_SCLS_NM": "만두/딤섬",
            "INVC_COUNT": "113326",
            "INVC_RANK": "21"
        },
        {
            "DL_YMW": "2022111",
            "DL_GD_SCLS_NM": "견과류",
            "INVC_COUNT": "113079",
            "INVC_RANK": "22"
        },
        {
            "DL_YMW": "2022111",
            "DL_GD_SCLS_NM": "조미료",
            "INVC_COUNT": "105921",
            "INVC_RANK": "23"
        },
        {
            "DL_YMW": "2022111",
            "DL_GD_SCLS_NM": "생선",
            "INVC_COUNT": "101039",
            "INVC_RANK": "24"
        },
        {
            "DL_YMW": "2022111",
            "DL_GD_SCLS_NM": "기타농산물",
            "INVC_COUNT": "86430",
            "INVC_RANK": "25"
        },
        {
            "DL_YMW": "2022111",
            "DL_GD_SCLS_NM": "건어물",
            "INVC_COUNT": "84808",
            "INVC_RANK": "26"
        },
        {
            "DL_YMW": "2022111",
            "DL_GD_SCLS_NM": "쇠고기",
            "INVC_COUNT": "77926",
            "INVC_RANK": "27"
        },
        {
            "DL_YMW": "2022111",
            "DL_GD_SCLS_NM": "두유",
            "INVC_COUNT": "77447",
            "INVC_RANK": "28"
        },
        {
            "DL_YMW": "2022111",
            "DL_GD_SCLS_NM": "김/해초",
            "INVC_COUNT": "72662",
            "INVC_RANK": "29"
        },
        {
            "DL_YMW": "2022111",
            "DL_GD_SCLS_NM": "라면",
            "INVC_COUNT": "70525",
            "INVC_RANK": "30"
        },
        {
            "DL_YMW": "2022104",
            "DL_GD_SCLS_NM": "과일",
            "INVC_COUNT": "654347",
            "INVC_RANK": "1"
        },
        {
            "DL_YMW": "2022104",
            "DL_GD_SCLS_NM": "영양제",
            "INVC_COUNT": "469881",
            "INVC_RANK": "2"
        },
        {
            "DL_YMW": "2022104",
            "DL_GD_SCLS_NM": "냉동/간편조리식품",
            "INVC_COUNT": "401124",
            "INVC_RANK": "3"
        },
        {
            "DL_YMW": "2022104",
            "DL_GD_SCLS_NM": "생수",
            "INVC_COUNT": "396388",
            "INVC_RANK": "4"
        },
        {
            "DL_YMW": "2022104",
            "DL_GD_SCLS_NM": "과자",
            "INVC_COUNT": "300657",
            "INVC_RANK": "5"
        },
        {
            "DL_YMW": "2022104",
            "DL_GD_SCLS_NM": "커피",
            "INVC_COUNT": "243493",
            "INVC_RANK": "6"
        },
        {
            "DL_YMW": "2022104",
            "DL_GD_SCLS_NM": "다이어트식품",
            "INVC_COUNT": "223733",
            "INVC_RANK": "7"
        },
        {
            "DL_YMW": "2022104",
            "DL_GD_SCLS_NM": "채소",
            "INVC_COUNT": "214293",
            "INVC_RANK": "8"
        },
        {
            "DL_YMW": "2022104",
            "DL_GD_SCLS_NM": "쌀/잡곡",
            "INVC_COUNT": "212117",
            "INVC_RANK": "9"
        },
        {
            "DL_YMW": "2022104",
            "DL_GD_SCLS_NM": "기타건강식품",
            "INVC_COUNT": "205366",
            "INVC_RANK": "10"
        },
        {
            "DL_YMW": "2022104",
            "DL_GD_SCLS_NM": "축산가공식품",
            "INVC_COUNT": "204282",
            "INVC_RANK": "11"
        },
        {
            "DL_YMW": "2022104",
            "DL_GD_SCLS_NM": "빵류/떡류",
            "INVC_COUNT": "193085",
            "INVC_RANK": "12"
        },
        {
            "DL_YMW": "2022104",
            "DL_GD_SCLS_NM": "유제품",
            "INVC_COUNT": "171254",
            "INVC_RANK": "13"
        },
        {
            "DL_YMW": "2022104",
            "DL_GD_SCLS_NM": "비타민제",
            "INVC_COUNT": "166293",
            "INVC_RANK": "14"
        },
        {
            "DL_YMW": "2022104",
            "DL_GD_SCLS_NM": "해산물/어패류",
            "INVC_COUNT": "163168",
            "INVC_RANK": "15"
        },
        {
            "DL_YMW": "2022104",
            "DL_GD_SCLS_NM": "기타식품",
            "INVC_COUNT": "162599",
            "INVC_RANK": "16"
        },
        {
            "DL_YMW": "2022104",
            "DL_GD_SCLS_NM": "탄산음료/탄산수",
            "INVC_COUNT": "123279",
            "INVC_RANK": "17"
        },
        {
            "DL_YMW": "2022104",
            "DL_GD_SCLS_NM": "차류",
            "INVC_COUNT": "121871",
            "INVC_RANK": "18"
        },
        {
            "DL_YMW": "2022104",
            "DL_GD_SCLS_NM": "포기김치",
            "INVC_COUNT": "121592",
            "INVC_RANK": "19"
        },
        {
            "DL_YMW": "2022104",
            "DL_GD_SCLS_NM": "즉석밥",
            "INVC_COUNT": "103458",
            "INVC_RANK": "20"
        },
        {
            "DL_YMW": "2022104",
            "DL_GD_SCLS_NM": "조미료",
            "INVC_COUNT": "101151",
            "INVC_RANK": "21"
        },
        {
            "DL_YMW": "2022104",
            "DL_GD_SCLS_NM": "견과류",
            "INVC_COUNT": "100648",
            "INVC_RANK": "22"
        },
        {
            "DL_YMW": "2022104",
            "DL_GD_SCLS_NM": "생선",
            "INVC_COUNT": "91526",
            "INVC_RANK": "23"
        },
        {
            "DL_YMW": "2022104",
            "DL_GD_SCLS_NM": "기타농산물",
            "INVC_COUNT": "80395",
            "INVC_RANK": "24"
        },
        {
            "DL_YMW": "2022104",
            "DL_GD_SCLS_NM": "만두/딤섬",
            "INVC_COUNT": "79205",
            "INVC_RANK": "25"
        },
        {
            "DL_YMW": "2022104",
            "DL_GD_SCLS_NM": "건어물",
            "INVC_COUNT": "73320",
            "INVC_RANK": "26"
        },
        {
            "DL_YMW": "2022104",
            "DL_GD_SCLS_NM": "쇠고기",
            "INVC_COUNT": "70521",
            "INVC_RANK": "27"
        },
        {
            "DL_YMW": "2022104",
            "DL_GD_SCLS_NM": "홍삼",
            "INVC_COUNT": "67972",
            "INVC_RANK": "28"
        },
        {
            "DL_YMW": "2022104",
            "DL_GD_SCLS_NM": "두유",
            "INVC_COUNT": "63746",
            "INVC_RANK": "29"
        },
        {
            "DL_YMW": "2022104",
            "DL_GD_SCLS_NM": "김/해초",
            "INVC_COUNT": "63295",
            "INVC_RANK": "30"
        },
        {
            "DL_YMW": "2022103",
            "DL_GD_SCLS_NM": "과일",
            "INVC_COUNT": "599821",
            "INVC_RANK": "1"
        },
        {
            "DL_YMW": "2022103",
            "DL_GD_SCLS_NM": "생수",
            "INVC_COUNT": "485246",
            "INVC_RANK": "2"
        },
        {
            "DL_YMW": "2022103",
            "DL_GD_SCLS_NM": "영양제",
            "INVC_COUNT": "470019",
            "INVC_RANK": "3"
        },
        {
            "DL_YMW": "2022103",
            "DL_GD_SCLS_NM": "냉동/간편조리식품",
            "INVC_COUNT": "393098",
            "INVC_RANK": "4"
        },
        {
            "DL_YMW": "2022103",
            "DL_GD_SCLS_NM": "과자",
            "INVC_COUNT": "290572",
            "INVC_RANK": "5"
        },
        {
            "DL_YMW": "2022103",
            "DL_GD_SCLS_NM": "커피",
            "INVC_COUNT": "244985",
            "INVC_RANK": "6"
        },
        {
            "DL_YMW": "2022103",
            "DL_GD_SCLS_NM": "쌀/잡곡",
            "INVC_COUNT": "226785",
            "INVC_RANK": "7"
        },
        {
            "DL_YMW": "2022103",
            "DL_GD_SCLS_NM": "다이어트식품",
            "INVC_COUNT": "221729",
            "INVC_RANK": "8"
        },
        {
            "DL_YMW": "2022103",
            "DL_GD_SCLS_NM": "채소",
            "INVC_COUNT": "221074",
            "INVC_RANK": "9"
        },
        {
            "DL_YMW": "2022103",
            "DL_GD_SCLS_NM": "축산가공식품",
            "INVC_COUNT": "218155",
            "INVC_RANK": "10"
        },
        {
            "DL_YMW": "2022103",
            "DL_GD_SCLS_NM": "기타건강식품",
            "INVC_COUNT": "211075",
            "INVC_RANK": "11"
        },
        {
            "DL_YMW": "2022103",
            "DL_GD_SCLS_NM": "빵류/떡류",
            "INVC_COUNT": "167829",
            "INVC_RANK": "12"
        },
        {
            "DL_YMW": "2022103",
            "DL_GD_SCLS_NM": "비타민제",
            "INVC_COUNT": "162178",
            "INVC_RANK": "13"
        },
        {
            "DL_YMW": "2022103",
            "DL_GD_SCLS_NM": "유제품",
            "INVC_COUNT": "161991",
            "INVC_RANK": "14"
        },
        {
            "DL_YMW": "2022103",
            "DL_GD_SCLS_NM": "기타식품",
            "INVC_COUNT": "150340",
            "INVC_RANK": "15"
        },
        {
            "DL_YMW": "2022103",
            "DL_GD_SCLS_NM": "해산물/어패류",
            "INVC_COUNT": "148643",
            "INVC_RANK": "16"
        },
        {
            "DL_YMW": "2022103",
            "DL_GD_SCLS_NM": "탄산음료/탄산수",
            "INVC_COUNT": "133896",
            "INVC_RANK": "17"
        },
        {
            "DL_YMW": "2022103",
            "DL_GD_SCLS_NM": "포기김치",
            "INVC_COUNT": "126250",
            "INVC_RANK": "18"
        },
        {
            "DL_YMW": "2022103",
            "DL_GD_SCLS_NM": "차류",
            "INVC_COUNT": "123997",
            "INVC_RANK": "19"
        },
        {
            "DL_YMW": "2022103",
            "DL_GD_SCLS_NM": "즉석밥",
            "INVC_COUNT": "102359",
            "INVC_RANK": "20"
        },
        {
            "DL_YMW": "2022103",
            "DL_GD_SCLS_NM": "견과류",
            "INVC_COUNT": "99066",
            "INVC_RANK": "21"
        },
        {
            "DL_YMW": "2022103",
            "DL_GD_SCLS_NM": "생선",
            "INVC_COUNT": "97603",
            "INVC_RANK": "22"
        },
        {
            "DL_YMW": "2022103",
            "DL_GD_SCLS_NM": "조미료",
            "INVC_COUNT": "95374",
            "INVC_RANK": "23"
        },
        {
            "DL_YMW": "2022103",
            "DL_GD_SCLS_NM": "만두/딤섬",
            "INVC_COUNT": "91672",
            "INVC_RANK": "24"
        },
        {
            "DL_YMW": "2022103",
            "DL_GD_SCLS_NM": "기타농산물",
            "INVC_COUNT": "76662",
            "INVC_RANK": "25"
        },
        {
            "DL_YMW": "2022103",
            "DL_GD_SCLS_NM": "두유",
            "INVC_COUNT": "68573",
            "INVC_RANK": "26"
        },
        {
            "DL_YMW": "2022103",
            "DL_GD_SCLS_NM": "김/해초",
            "INVC_COUNT": "67761",
            "INVC_RANK": "27"
        },
        {
            "DL_YMW": "2022103",
            "DL_GD_SCLS_NM": "홍삼",
            "INVC_COUNT": "65729",
            "INVC_RANK": "28"
        },
        {
            "DL_YMW": "2022103",
            "DL_GD_SCLS_NM": "라면",
            "INVC_COUNT": "62665",
            "INVC_RANK": "29"
        },
        {
            "DL_YMW": "2022103",
            "DL_GD_SCLS_NM": "주스/과즙음료",
            "INVC_COUNT": "60623",
            "INVC_RANK": "30"
        },
        {
            "DL_YMW": "2022102",
            "DL_GD_SCLS_NM": "과일",
            "INVC_COUNT": "504389",
            "INVC_RANK": "1"
        },
        {
            "DL_YMW": "2022102",
            "DL_GD_SCLS_NM": "생수",
            "INVC_COUNT": "503260",
            "INVC_RANK": "2"
        },
        {
            "DL_YMW": "2022102",
            "DL_GD_SCLS_NM": "영양제",
            "INVC_COUNT": "461563",
            "INVC_RANK": "3"
        },
        {
            "DL_YMW": "2022102",
            "DL_GD_SCLS_NM": "냉동/간편조리식품",
            "INVC_COUNT": "379438",
            "INVC_RANK": "4"
        },
        {
            "DL_YMW": "2022102",
            "DL_GD_SCLS_NM": "과자",
            "INVC_COUNT": "237867",
            "INVC_RANK": "5"
        },
        {
            "DL_YMW": "2022102",
            "DL_GD_SCLS_NM": "커피",
            "INVC_COUNT": "234380",
            "INVC_RANK": "6"
        },
        {
            "DL_YMW": "2022102",
            "DL_GD_SCLS_NM": "채소",
            "INVC_COUNT": "213099",
            "INVC_RANK": "7"
        },
        {
            "DL_YMW": "2022102",
            "DL_GD_SCLS_NM": "축산가공식품",
            "INVC_COUNT": "209083",
            "INVC_RANK": "8"
        },
        {
            "DL_YMW": "2022102",
            "DL_GD_SCLS_NM": "다이어트식품",
            "INVC_COUNT": "206640",
            "INVC_RANK": "9"
        },
        {
            "DL_YMW": "2022102",
            "DL_GD_SCLS_NM": "쌀/잡곡",
            "INVC_COUNT": "197083",
            "INVC_RANK": "10"
        },
        {
            "DL_YMW": "2022102",
            "DL_GD_SCLS_NM": "기타건강식품",
            "INVC_COUNT": "193999",
            "INVC_RANK": "11"
        },
        {
            "DL_YMW": "2022102",
            "DL_GD_SCLS_NM": "기타식품",
            "INVC_COUNT": "192415",
            "INVC_RANK": "12"
        },
        {
            "DL_YMW": "2022102",
            "DL_GD_SCLS_NM": "비타민제",
            "INVC_COUNT": "166992",
            "INVC_RANK": "13"
        },
        {
            "DL_YMW": "2022102",
            "DL_GD_SCLS_NM": "빵류/떡류",
            "INVC_COUNT": "164177",
            "INVC_RANK": "14"
        },
        {
            "DL_YMW": "2022102",
            "DL_GD_SCLS_NM": "해산물/어패류",
            "INVC_COUNT": "160725",
            "INVC_RANK": "15"
        },
        {
            "DL_YMW": "2022102",
            "DL_GD_SCLS_NM": "탄산음료/탄산수",
            "INVC_COUNT": "132577",
            "INVC_RANK": "16"
        },
        {
            "DL_YMW": "2022102",
            "DL_GD_SCLS_NM": "차류",
            "INVC_COUNT": "122574",
            "INVC_RANK": "17"
        },
        {
            "DL_YMW": "2022102",
            "DL_GD_SCLS_NM": "포기김치",
            "INVC_COUNT": "120043",
            "INVC_RANK": "18"
        },
        {
            "DL_YMW": "2022102",
            "DL_GD_SCLS_NM": "유제품",
            "INVC_COUNT": "111448",
            "INVC_RANK": "19"
        },
        {
            "DL_YMW": "2022102",
            "DL_GD_SCLS_NM": "조미료",
            "INVC_COUNT": "103039",
            "INVC_RANK": "20"
        },
        {
            "DL_YMW": "2022102",
            "DL_GD_SCLS_NM": "즉석밥",
            "INVC_COUNT": "91524",
            "INVC_RANK": "21"
        },
        {
            "DL_YMW": "2022102",
            "DL_GD_SCLS_NM": "견과류",
            "INVC_COUNT": "90683",
            "INVC_RANK": "22"
        },
        {
            "DL_YMW": "2022102",
            "DL_GD_SCLS_NM": "만두/딤섬",
            "INVC_COUNT": "90634",
            "INVC_RANK": "23"
        },
        {
            "DL_YMW": "2022102",
            "DL_GD_SCLS_NM": "두유",
            "INVC_COUNT": "83932",
            "INVC_RANK": "24"
        },
        {
            "DL_YMW": "2022102",
            "DL_GD_SCLS_NM": "생선",
            "INVC_COUNT": "82716",
            "INVC_RANK": "25"
        },
        {
            "DL_YMW": "2022102",
            "DL_GD_SCLS_NM": "쇠고기",
            "INVC_COUNT": "65234",
            "INVC_RANK": "26"
        },
        {
            "DL_YMW": "2022102",
            "DL_GD_SCLS_NM": "기타농산물",
            "INVC_COUNT": "64789",
            "INVC_RANK": "27"
        },
        {
            "DL_YMW": "2022102",
            "DL_GD_SCLS_NM": "홍삼",
            "INVC_COUNT": "60854",
            "INVC_RANK": "28"
        },
        {
            "DL_YMW": "2022102",
            "DL_GD_SCLS_NM": "주스/과즙음료",
            "INVC_COUNT": "59634",
            "INVC_RANK": "29"
        },
        {
            "DL_YMW": "2022102",
            "DL_GD_SCLS_NM": "김/해초",
            "INVC_COUNT": "58805",
            "INVC_RANK": "30"
        }
    ]

@app.get("/data/102",tags=["102"])
async  def data_102():
    return [
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.5590"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.6446"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.6448"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.6501"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.6865"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.6867"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.7009"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.7062"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.7074"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.7157"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.7241"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.7430"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.7447"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.7549"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.7553"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.7566"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.7579"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.7743"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.7751"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.7755"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.7784"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.7815"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.7927"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.7937"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.7961"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8087"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8105"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.8107"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8123"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8131"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.8153"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.8164"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.8200"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8209"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8229"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8234"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8264"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8280"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.8285"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.8317"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.8324"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.8331"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8350"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8361"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.8376"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8377"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.8462"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.8468"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.8470"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8513"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.8547"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.8552"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.8639"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.8696"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.8721"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8733"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.8746"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8764"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8768"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.8778"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.8788"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8811"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.8813"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.8836"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.8914"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "인천",
            "ACHIV_RAT": "0.8930"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.8955"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8973"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.8977"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8984"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.9015"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9018"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9033"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9037"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.9099"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9125"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "서울",
            "ACHIV_RAT": "0.9127"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.9138"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.9166"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.9199"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9261"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9277"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9280"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.9323"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.9393"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.9416"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "서울",
            "ACHIV_RAT": "0.9472"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.9487"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.9506"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.9507"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9556"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9562"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9654"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.9737"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "서울",
            "ACHIV_RAT": "0.9743"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.9749"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.9751"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9764"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9768"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.9791"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.9816"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.9851"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.9860"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.9888"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.9895"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9909"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9932"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "서울",
            "ACHIV_RAT": "0.9989"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0007"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0031"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "대전",
            "ACHIV_RAT": "1.0048"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0053"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.0066"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.0087"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.0094"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0104"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.0108"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.0117"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0120"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.0124"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.0168"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.0225"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "전북",
            "ACHIV_RAT": "1.0246"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0274"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.0302"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.0341"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "대전",
            "ACHIV_RAT": "1.0453"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "대전",
            "ACHIV_RAT": "1.0478"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "경남",
            "ACHIV_RAT": "1.0502"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.0553"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0583"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.0639"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.0668"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.0678"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "강원",
            "ACHIV_RAT": "1.0697"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "강원",
            "ACHIV_RAT": "1.0752"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0762"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0778"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0822"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.0833"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.0907"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.0949"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0959"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.0963"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0969"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "울산",
            "ACHIV_RAT": "1.1043"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.1046"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "강원",
            "ACHIV_RAT": "1.1106"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.1197"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.1228"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.1248"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.1326"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.1368"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.1613"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.1681"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "강원",
            "ACHIV_RAT": "1.1764"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.1806"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.1994"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "경남",
            "ACHIV_RAT": "1.2111"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.2247"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.2512"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.2572"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.3041"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.3090"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.3376"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.3566"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "경남",
            "ACHIV_RAT": "1.3992"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.6710"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "울산",
            "ACHIV_RAT": "1.6731"
        },
        {
            "WEEK_BEGIN_DT": "20230213",
            "WEEK_END_DT": "20230219",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.8474"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.6066"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.6493"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.6587"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.6668"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.6824"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.6860"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.6910"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.7014"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.7031"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.7038"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.7080"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.7105"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.7145"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.7160"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.7224"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.7274"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.7459"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.7475"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.7523"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.7648"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.7805"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.7931"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.7949"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.7981"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.7986"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.7994"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.8002"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8045"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.8063"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8085"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.8087"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.8111"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8114"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.8135"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8143"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.8174"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8219"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.8264"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.8302"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8324"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8335"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.8346"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8367"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.8390"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.8410"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.8431"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.8452"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.8479"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8481"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.8481"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8492"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.8531"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8569"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.8631"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.8632"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8633"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.8637"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.8640"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.8640"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.8656"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.8707"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8707"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.8734"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.8831"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8835"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8872"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8902"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.8904"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8960"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.8970"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.9027"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.9032"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.9041"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.9084"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.9102"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "인천",
            "ACHIV_RAT": "0.9106"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9140"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9152"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9183"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9190"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9193"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.9195"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.9199"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9204"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "서울",
            "ACHIV_RAT": "0.9221"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.9378"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9456"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "서울",
            "ACHIV_RAT": "0.9479"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9482"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9493"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.9591"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.9596"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.9600"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "서울",
            "ACHIV_RAT": "0.9653"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9680"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9722"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9738"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.9760"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.9782"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9816"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "인천",
            "ACHIV_RAT": "0.9918"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9926"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.9964"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.9977"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "강원",
            "ACHIV_RAT": "1.0000"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.0025"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.0037"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "전북",
            "ACHIV_RAT": "1.0042"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.0064"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0065"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0085"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0094"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.0113"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.0119"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.0140"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "강원",
            "ACHIV_RAT": "1.0164"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.0173"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.0182"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0185"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.0218"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0220"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.0228"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.0244"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.0247"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.0257"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.0279"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "대전",
            "ACHIV_RAT": "1.0282"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.0288"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.0314"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "전북",
            "ACHIV_RAT": "1.0320"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.0370"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.0459"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.0561"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "경남",
            "ACHIV_RAT": "1.0578"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "대전",
            "ACHIV_RAT": "1.0585"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "경남",
            "ACHIV_RAT": "1.0637"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.0644"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.0734"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.0758"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "울산",
            "ACHIV_RAT": "1.0801"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0804"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0827"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0845"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "강원",
            "ACHIV_RAT": "1.0876"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.0904"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0906"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.0944"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.0948"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.1021"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.1091"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "강원",
            "ACHIV_RAT": "1.1248"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.1294"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.1376"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.1632"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.1742"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.1754"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.1881"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.1926"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.2167"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.2289"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.2354"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.2390"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.2703"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.3317"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.3460"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.3554"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "경남",
            "ACHIV_RAT": "1.4067"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.6861"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.7232"
        },
        {
            "WEEK_BEGIN_DT": "20230206",
            "WEEK_END_DT": "20230212",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "울산",
            "ACHIV_RAT": "1.7265"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.5896"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.6226"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.6794"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.6811"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.6866"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.7023"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.7025"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.7123"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.7142"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.7166"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.7197"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.7277"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.7428"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.7432"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.7439"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.7484"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.7583"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.7586"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.7594"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.7628"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.7638"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.7679"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.7750"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.7760"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.7799"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.7805"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.7814"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.7887"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.7908"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.7976"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.7985"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8054"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.8072"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.8125"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.8152"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8153"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.8156"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8238"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.8283"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8287"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8313"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.8326"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8331"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.8404"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8406"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.8428"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.8433"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.8448"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.8464"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.8478"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.8494"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.8554"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.8569"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.8570"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.8583"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.8613"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.8649"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.8651"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.8654"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.8713"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8722"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8739"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8746"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8764"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8780"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8823"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8831"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8847"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8941"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8968"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.8988"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9003"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.9022"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.9030"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.9033"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9059"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.9063"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9080"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9099"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9127"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.9163"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9165"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9166"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "서울",
            "ACHIV_RAT": "0.9239"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "서울",
            "ACHIV_RAT": "0.9270"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9289"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "인천",
            "ACHIV_RAT": "0.9310"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.9311"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9383"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "서울",
            "ACHIV_RAT": "0.9400"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.9407"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.9433"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.9444"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.9486"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.9513"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.9516"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "인천",
            "ACHIV_RAT": "0.9544"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9545"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.9652"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9728"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9745"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "인천",
            "ACHIV_RAT": "0.9761"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.9825"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.9829"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.9845"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "인천",
            "ACHIV_RAT": "0.9884"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.9891"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "서울",
            "ACHIV_RAT": "0.9914"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9970"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "인천",
            "ACHIV_RAT": "0.9971"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9975"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9984"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.9988"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0006"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "울산",
            "ACHIV_RAT": "1.0016"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "전북",
            "ACHIV_RAT": "1.0062"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0065"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.0141"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.0189"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "대전",
            "ACHIV_RAT": "1.0190"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.0207"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.0256"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0296"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.0353"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.0395"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.0407"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.0417"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.0442"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.0473"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0475"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.0476"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.0479"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.0571"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "대전",
            "ACHIV_RAT": "1.0583"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.0709"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.0809"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0831"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0852"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "광주",
            "ACHIV_RAT": "1.0871"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0872"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0886"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.0897"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.0934"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.0958"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.0992"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.1056"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.1101"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "강원",
            "ACHIV_RAT": "1.1109"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.1272"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "강원",
            "ACHIV_RAT": "1.1284"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.1292"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.1302"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.1402"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.1619"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.2008"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.2121"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.2247"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.2372"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.2437"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "경남",
            "ACHIV_RAT": "1.2532"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.2607"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.3504"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.3716"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.3839"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "경남",
            "ACHIV_RAT": "1.3950"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.4639"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.5464"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "강원",
            "ACHIV_RAT": "1.7186"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "울산",
            "ACHIV_RAT": "2.0461"
        },
        {
            "WEEK_BEGIN_DT": "20230130",
            "WEEK_END_DT": "20230205",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "울산",
            "ACHIV_RAT": "3.2866"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.3784"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.5705"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.6292"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.6393"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.6584"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.7028"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.7136"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.7220"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.7256"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.7388"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.7521"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.7771"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.7786"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.7842"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.7844"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.7847"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.7865"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.7909"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.7962"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.7966"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.7968"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.7972"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8072"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.8091"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.8115"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.8145"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.8158"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.8197"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.8201"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.8219"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.8251"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.8259"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8266"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.8270"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8294"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.8332"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8335"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.8394"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.8410"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.8450"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.8452"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.8500"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.8529"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.8537"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8637"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.8640"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8656"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.8660"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8681"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.8721"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.8804"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.8808"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.8808"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8814"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8850"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.8864"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.8872"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.8904"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.8919"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8925"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8947"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8970"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.8983"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "인천",
            "ACHIV_RAT": "0.9003"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.9014"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.9020"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "서울",
            "ACHIV_RAT": "0.9038"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9038"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.9077"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9078"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.9108"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "서울",
            "ACHIV_RAT": "0.9144"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9174"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.9181"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9195"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9265"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9315"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.9361"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9364"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9376"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.9396"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.9415"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9423"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.9468"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.9503"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.9508"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.9521"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9538"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.9564"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9589"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.9604"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9610"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "서울",
            "ACHIV_RAT": "0.9620"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9633"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.9687"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.9705"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9724"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9782"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.9813"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.9814"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.9823"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9834"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9853"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9869"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9927"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "서울",
            "ACHIV_RAT": "0.9974"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.0001"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.0019"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.0022"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "광주",
            "ACHIV_RAT": "1.0064"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "전북",
            "ACHIV_RAT": "1.0066"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "전북",
            "ACHIV_RAT": "1.0097"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0116"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0120"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0148"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.0152"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0176"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.0251"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.0294"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.0304"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.0307"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "대전",
            "ACHIV_RAT": "1.0354"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.0393"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0472"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.0474"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.0506"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.0534"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.0542"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0546"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "경남",
            "ACHIV_RAT": "1.0550"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.0558"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.0592"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "강원",
            "ACHIV_RAT": "1.0653"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "전북",
            "ACHIV_RAT": "1.0673"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.0712"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.0725"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.0837"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.0891"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0905"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.0909"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0915"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.0927"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0936"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0962"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.0967"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.1045"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.1053"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "강원",
            "ACHIV_RAT": "1.1110"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.1118"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "강원",
            "ACHIV_RAT": "1.1146"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.1209"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.1553"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.1702"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.1702"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.1769"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.1867"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "강원",
            "ACHIV_RAT": "1.1908"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "경남",
            "ACHIV_RAT": "1.2073"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.2178"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.2424"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.2653"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "경남",
            "ACHIV_RAT": "1.2677"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.2949"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.3078"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.3611"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.3649"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.4820"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.5014"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.5218"
        },
        {
            "WEEK_BEGIN_DT": "20230123",
            "WEEK_END_DT": "20230129",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "울산",
            "ACHIV_RAT": "2.1375"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.5321"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.6845"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.6930"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.7064"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.7089"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.7093"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.7171"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.7176"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.7240"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.7288"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.7374"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.7448"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.7536"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.7560"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.7717"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.7724"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.7752"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.7820"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.7828"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.7879"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.7960"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.7986"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.8011"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8012"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.8056"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8064"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8065"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.8112"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8123"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8140"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.8153"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.8158"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.8166"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8192"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.8193"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.8195"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.8213"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.8214"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.8229"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8231"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.8251"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.8269"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8276"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.8287"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8347"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.8382"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8395"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8399"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.8402"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.8402"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.8413"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.8414"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.8458"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8458"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8489"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.8519"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8540"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8565"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8586"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.8642"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.8653"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.8739"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8783"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.8801"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "인천",
            "ACHIV_RAT": "0.8860"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8901"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.8925"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8941"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.8981"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.8985"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9016"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.9093"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "서울",
            "ACHIV_RAT": "0.9096"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9109"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9130"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9175"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9180"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9193"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.9211"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "인천",
            "ACHIV_RAT": "0.9237"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9266"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9295"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "서울",
            "ACHIV_RAT": "0.9385"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.9445"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9491"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.9499"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "서울",
            "ACHIV_RAT": "0.9503"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9521"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.9522"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9536"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9583"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9595"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9609"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.9626"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.9649"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.9671"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9716"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.9794"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9796"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9814"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.9839"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9881"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9901"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.9902"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.9911"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.9969"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.9976"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9981"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "인천",
            "ACHIV_RAT": "0.9994"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0018"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0018"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.0053"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.0064"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.0116"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "경남",
            "ACHIV_RAT": "1.0121"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0128"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.0165"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.0167"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.0189"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.0198"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.0226"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0243"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "전북",
            "ACHIV_RAT": "1.0283"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "대전",
            "ACHIV_RAT": "1.0304"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.0328"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.0339"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.0341"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0376"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.0397"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.0423"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.0448"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "강원",
            "ACHIV_RAT": "1.0511"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "경남",
            "ACHIV_RAT": "1.0559"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.0564"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.0596"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "울산",
            "ACHIV_RAT": "1.0613"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.0720"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0724"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.0729"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0789"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0834"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0845"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.0861"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0881"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "강원",
            "ACHIV_RAT": "1.0893"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.0986"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.1049"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.1066"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.1168"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.1382"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.1389"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.1409"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.1545"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.1573"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.1713"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.1737"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.1832"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.2030"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.2206"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.2577"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "경남",
            "ACHIV_RAT": "1.2671"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.2740"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.3112"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.3390"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.3416"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.3463"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.4582"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "경남",
            "ACHIV_RAT": "1.5868"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.7152"
        },
        {
            "WEEK_BEGIN_DT": "20230116",
            "WEEK_END_DT": "20230122",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "울산",
            "ACHIV_RAT": "1.7655"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.5670"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.6337"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.6780"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.6933"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.6968"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.6993"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.7100"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.7128"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.7159"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.7359"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.7374"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.7402"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.7414"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.7482"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.7535"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.7605"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.7614"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.7661"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.7722"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.7768"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.7868"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.7870"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.7926"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.7942"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.7951"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8008"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8041"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8091"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8125"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8138"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8168"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.8173"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.8179"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.8185"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8191"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.8200"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.8206"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8208"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.8217"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.8239"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8291"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.8295"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8298"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8306"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.8329"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.8363"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8385"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8396"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8397"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.8411"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.8416"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.8484"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.8518"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.8534"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.8540"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.8546"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.8567"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8570"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8613"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8636"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8684"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8752"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.8764"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.8770"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.8790"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.8817"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.8906"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8911"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.8914"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.8925"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8984"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "인천",
            "ACHIV_RAT": "0.8992"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9004"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9047"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9058"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9086"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9118"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9121"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9141"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.9144"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9183"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "서울",
            "ACHIV_RAT": "0.9211"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.9291"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9291"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9299"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "서울",
            "ACHIV_RAT": "0.9304"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9361"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.9378"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "서울",
            "ACHIV_RAT": "0.9378"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.9436"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "인천",
            "ACHIV_RAT": "0.9472"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.9479"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9537"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9571"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.9605"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.9624"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9672"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.9696"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.9707"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.9716"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9734"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9754"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9795"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.9835"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9909"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.9921"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "인천",
            "ACHIV_RAT": "0.9944"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.9964"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9966"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.9967"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9968"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.9984"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0044"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "전북",
            "ACHIV_RAT": "1.0074"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.0082"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0092"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0108"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "강원",
            "ACHIV_RAT": "1.0141"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0165"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.0176"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.0209"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.0233"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0253"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "경남",
            "ACHIV_RAT": "1.0273"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.0278"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.0279"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.0311"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.0333"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.0360"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.0364"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.0418"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "대전",
            "ACHIV_RAT": "1.0437"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "울산",
            "ACHIV_RAT": "1.0554"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "강원",
            "ACHIV_RAT": "1.0596"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0668"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0711"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.0711"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.0774"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.0791"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0879"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "강원",
            "ACHIV_RAT": "1.0889"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0950"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0987"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.1000"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.1004"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.1124"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "경남",
            "ACHIV_RAT": "1.1160"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.1280"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.1311"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "전북",
            "ACHIV_RAT": "1.1319"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.1391"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.1466"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.1544"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.1671"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.1790"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.1922"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.1985"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.2068"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.2384"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.2519"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.2587"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "경남",
            "ACHIV_RAT": "1.2826"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.3247"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.3406"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.3435"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.3539"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.3746"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "울산",
            "ACHIV_RAT": "1.4827"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.5474"
        },
        {
            "WEEK_BEGIN_DT": "20230109",
            "WEEK_END_DT": "20230115",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.5842"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.5259"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.6358"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.6423"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.6658"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.6947"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.7058"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.7061"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.7107"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.7213"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.7228"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.7253"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.7254"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.7360"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.7428"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.7493"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.7585"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.7612"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.7764"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.7769"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.7781"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.7805"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.7859"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.7889"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.7914"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.8029"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.8084"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.8129"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8130"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8131"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.8152"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.8155"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.8192"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.8202"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8265"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.8270"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8280"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8280"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8287"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8308"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.8310"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.8312"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8341"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.8374"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8375"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.8394"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.8398"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.8414"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8431"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.8433"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.8443"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.8445"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8464"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8471"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.8481"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.8509"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.8570"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.8583"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.8609"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.8618"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8627"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8663"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.8681"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.8690"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.8752"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "인천",
            "ACHIV_RAT": "0.8772"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8780"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8792"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.8844"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.8912"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8940"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.8944"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.8950"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8981"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.9038"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9054"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "서울",
            "ACHIV_RAT": "0.9054"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9072"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9135"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.9158"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9168"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9231"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.9276"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.9278"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9292"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9338"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.9342"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9355"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9391"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9479"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.9527"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.9575"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.9598"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "서울",
            "ACHIV_RAT": "0.9617"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "인천",
            "ACHIV_RAT": "0.9622"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.9641"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.9644"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.9657"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9712"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9739"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.9745"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.9814"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9834"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9835"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9847"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9899"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "인천",
            "ACHIV_RAT": "0.9905"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.9909"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.9930"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.9935"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.9972"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.9997"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0028"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "대전",
            "ACHIV_RAT": "1.0042"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0050"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.0089"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.0109"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.0111"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.0112"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0124"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.0131"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0166"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.0180"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.0225"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.0305"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0335"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.0344"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "경남",
            "ACHIV_RAT": "1.0379"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.0484"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "강원",
            "ACHIV_RAT": "1.0514"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "울산",
            "ACHIV_RAT": "1.0524"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.0534"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.0538"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.0642"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "전북",
            "ACHIV_RAT": "1.0654"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0668"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.0691"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0731"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0763"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.0791"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "강원",
            "ACHIV_RAT": "1.0792"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.0802"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.0825"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0867"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0927"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0970"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.1038"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "울산",
            "ACHIV_RAT": "1.1144"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.1162"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.1166"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.1225"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.1526"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "강원",
            "ACHIV_RAT": "1.1548"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.1627"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.1723"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.1729"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "경남",
            "ACHIV_RAT": "1.1765"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.1852"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.1864"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.1931"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "경남",
            "ACHIV_RAT": "1.2099"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.2112"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.2421"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.2565"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.2719"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.3072"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.3363"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.3400"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.3689"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.5531"
        },
        {
            "WEEK_BEGIN_DT": "20230102",
            "WEEK_END_DT": "20230108",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "울산",
            "ACHIV_RAT": "1.8827"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.5333"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.5453"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.5958"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.5967"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.6282"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.6435"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.6544"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.6588"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.6815"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.6890"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.6985"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.7053"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.7164"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.7197"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.7371"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.7378"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.7392"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.7423"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.7440"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.7450"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.7553"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.7641"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.7641"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.7663"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.7711"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.7735"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.7822"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.7879"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.7937"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.7970"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.7983"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.7998"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.8004"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.8015"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8015"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.8023"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.8074"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.8088"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.8168"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.8192"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8202"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.8206"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.8245"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8273"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "인천",
            "ACHIV_RAT": "0.8313"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8324"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8345"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8345"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.8389"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.8392"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.8410"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.8421"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8434"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8451"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.8483"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8486"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.8526"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.8555"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.8567"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.8581"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8584"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.8593"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.8593"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8604"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8626"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8628"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.8656"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.8668"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8690"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8706"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.8743"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "서울",
            "ACHIV_RAT": "0.8766"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.8769"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.8790"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.8878"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.8879"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.8881"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "서울",
            "ACHIV_RAT": "0.8979"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.8996"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9037"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9066"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.9075"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9118"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9127"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9161"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9246"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.9304"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9313"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.9315"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "서울",
            "ACHIV_RAT": "0.9336"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9357"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.9432"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.9518"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.9523"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.9541"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.9550"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.9555"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.9560"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.9567"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9616"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.9656"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.9665"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.9681"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9691"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.9753"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.9788"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.9790"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "인천",
            "ACHIV_RAT": "0.9801"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9834"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9840"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9842"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9930"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "인천",
            "ACHIV_RAT": "0.9937"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.9968"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9979"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.0048"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.0055"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0079"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0090"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.0125"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.0133"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0254"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.0255"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "경남",
            "ACHIV_RAT": "1.0372"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0417"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0433"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "경남",
            "ACHIV_RAT": "1.0487"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.0604"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.0658"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.0662"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.0680"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0791"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.0855"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "강원",
            "ACHIV_RAT": "1.0871"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0874"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.0887"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0922"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0933"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "울산",
            "ACHIV_RAT": "1.0939"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.0950"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.0986"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.0995"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.1051"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.1075"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "강원",
            "ACHIV_RAT": "1.1083"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.1121"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.1124"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.1142"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.1249"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.1259"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.1314"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.1353"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "강원",
            "ACHIV_RAT": "1.1375"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.1425"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.1541"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.1620"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.1654"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "강원",
            "ACHIV_RAT": "1.1668"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.2029"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "경남",
            "ACHIV_RAT": "1.2149"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.2374"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.3177"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.3223"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.3317"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.4537"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.5159"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.9584"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "대전",
            "ACHIV_RAT": "2.1559"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "울산",
            "ACHIV_RAT": "2.3111"
        },
        {
            "WEEK_BEGIN_DT": "20221226",
            "WEEK_END_DT": "20230101",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "울산",
            "ACHIV_RAT": "4.1238"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.4787"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.6276"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.6392"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.6799"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.6923"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.7134"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.7142"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.7158"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.7164"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.7215"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.7303"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.7451"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.7498"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.7509"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.7560"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.7564"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.7597"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.7601"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.7619"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.7752"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.7768"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.7801"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.7819"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.7824"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.7833"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.7835"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.7924"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.7967"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.7977"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8068"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8072"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.8092"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8094"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8116"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8151"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.8160"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8255"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.8268"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8285"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.8326"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.8342"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.8354"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.8388"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.8409"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8439"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.8442"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.8461"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.8516"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.8548"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.8587"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.8599"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8601"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.8602"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8632"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.8632"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8671"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8684"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8711"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.8712"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8719"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8760"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "인천",
            "ACHIV_RAT": "0.8765"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.8775"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8789"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.8810"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8845"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.8861"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8928"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.8947"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.8971"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.8983"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.9021"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.9083"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9103"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9113"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.9120"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "서울",
            "ACHIV_RAT": "0.9180"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.9232"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9244"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9269"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "서울",
            "ACHIV_RAT": "0.9292"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9307"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9312"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.9313"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.9314"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9324"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9341"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9413"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.9429"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.9439"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.9442"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.9545"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9571"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.9631"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9669"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.9684"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9699"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.9734"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.9737"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.9745"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9781"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.9809"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.9809"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.9823"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.9833"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "인천",
            "ACHIV_RAT": "0.9925"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9942"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9976"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.0022"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.0065"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.0070"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0077"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "광주",
            "ACHIV_RAT": "1.0084"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.0085"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "대전",
            "ACHIV_RAT": "1.0096"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "대전",
            "ACHIV_RAT": "1.0100"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.0103"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.0142"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.0186"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.0203"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0225"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "경남",
            "ACHIV_RAT": "1.0293"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.0307"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.0335"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0368"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.0392"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "울산",
            "ACHIV_RAT": "1.0417"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.0431"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "강원",
            "ACHIV_RAT": "1.0435"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0459"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0535"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.0564"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.0582"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0593"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "광주",
            "ACHIV_RAT": "1.0598"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.0606"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.0636"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0646"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "대전",
            "ACHIV_RAT": "1.0712"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "강원",
            "ACHIV_RAT": "1.0745"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0766"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.0777"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0872"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.0920"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.1001"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.1043"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.1050"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.1057"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.1091"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.1205"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.1363"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.1553"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "강원",
            "ACHIV_RAT": "1.1564"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "경남",
            "ACHIV_RAT": "1.1572"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.1622"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "광주",
            "ACHIV_RAT": "1.1698"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.1723"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.1743"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.1851"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.1942"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.2539"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.2801"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.3543"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.3590"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.3596"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.4013"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "경남",
            "ACHIV_RAT": "1.4358"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.4744"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.5605"
        },
        {
            "WEEK_BEGIN_DT": "20221219",
            "WEEK_END_DT": "20221225",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "울산",
            "ACHIV_RAT": "1.8435"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.4655"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.6510"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.6597"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.6806"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.7024"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.7155"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.7199"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.7276"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.7379"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.7425"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.7426"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.7433"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.7566"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.7630"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.7653"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.7664"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.7698"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.7709"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.7716"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.7738"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.7775"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.7778"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.7820"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.7823"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.7888"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.8025"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8057"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8102"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8105"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8108"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.8140"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.8174"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8181"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8184"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8196"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.8231"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.8245"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.8246"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.8264"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8274"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8403"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.8440"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.8447"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.8475"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8492"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.8495"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8503"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8515"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.8562"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.8581"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.8591"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8605"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.8630"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.8674"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.8679"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.8679"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.8688"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.8719"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8726"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "인천",
            "ACHIV_RAT": "0.8809"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.8823"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.8826"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.8841"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.8864"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.8868"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8915"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.8920"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8946"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.8949"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.8964"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.8987"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9093"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.9139"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9176"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.9207"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.9221"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "서울",
            "ACHIV_RAT": "0.9252"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9261"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "서울",
            "ACHIV_RAT": "0.9327"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.9362"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.9399"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.9437"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9450"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9451"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.9461"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9487"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.9532"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "서울",
            "ACHIV_RAT": "0.9569"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.9580"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.9582"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9686"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.9706"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "인천",
            "ACHIV_RAT": "0.9731"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9750"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "인천",
            "ACHIV_RAT": "0.9765"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.9779"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.9781"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9791"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.9806"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.9830"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9856"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9864"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9877"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9934"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.9948"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.9963"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9976"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0017"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.0017"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.0085"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.0097"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0130"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "강원",
            "ACHIV_RAT": "1.0141"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.0142"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.0144"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "대전",
            "ACHIV_RAT": "1.0149"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "경남",
            "ACHIV_RAT": "1.0156"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0188"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.0202"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.0204"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.0246"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.0248"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.0262"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.0283"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0302"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.0308"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.0357"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "강원",
            "ACHIV_RAT": "1.0383"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.0391"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.0397"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0428"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.0447"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "대전",
            "ACHIV_RAT": "1.0539"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0560"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.0592"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0602"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.0631"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0658"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.0686"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.0689"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.0716"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0732"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "대전",
            "ACHIV_RAT": "1.0752"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.0774"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0800"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "광주",
            "ACHIV_RAT": "1.0857"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.1007"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.1077"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.1141"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.1145"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.1235"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.1242"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "강원",
            "ACHIV_RAT": "1.1310"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.1505"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "경남",
            "ACHIV_RAT": "1.1606"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.1698"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.2050"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.2101"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.2413"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.2631"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.2670"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.2870"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.3037"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.3258"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.3301"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.3348"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "경남",
            "ACHIV_RAT": "1.4003"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.4522"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "울산",
            "ACHIV_RAT": "1.5128"
        },
        {
            "WEEK_BEGIN_DT": "20221212",
            "WEEK_END_DT": "20221218",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "대구",
            "ACHIV_RAT": "2.2427"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.4756"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.6023"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.6481"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.6626"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.6971"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.7039"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.7285"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.7349"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.7362"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.7362"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.7394"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.7421"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.7438"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.7540"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.7609"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.7618"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.7632"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.7690"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.7748"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.7867"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.7869"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.7869"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.7913"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.7925"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.7932"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.7976"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.8016"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8042"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8095"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8127"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8151"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.8167"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8189"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.8202"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8205"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8218"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8220"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.8224"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8250"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.8252"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.8290"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8304"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.8348"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8376"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8455"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8502"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.8545"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.8598"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8625"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8627"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8674"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.8689"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.8701"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8712"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.8733"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.8764"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.8767"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.8813"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.8816"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.8846"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8900"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.8925"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.8950"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.8954"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.8986"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9007"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9025"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.9042"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9102"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "서울",
            "ACHIV_RAT": "0.9170"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.9176"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "인천",
            "ACHIV_RAT": "0.9185"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9201"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9203"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.9228"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.9247"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.9330"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9335"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "서울",
            "ACHIV_RAT": "0.9335"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.9368"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9370"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9391"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9413"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.9415"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.9419"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9433"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.9467"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.9470"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.9485"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9486"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9533"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.9552"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.9641"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9671"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.9688"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.9697"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9722"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9760"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.9831"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9867"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9900"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.9904"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9904"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "서울",
            "ACHIV_RAT": "0.9905"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.9938"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.9959"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9984"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.0032"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "전북",
            "ACHIV_RAT": "1.0051"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.0071"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0082"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0082"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0149"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.0158"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.0164"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0177"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0192"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.0202"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.0205"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "강원",
            "ACHIV_RAT": "1.0206"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "대전",
            "ACHIV_RAT": "1.0237"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.0252"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.0289"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.0330"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.0350"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.0380"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.0394"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "강원",
            "ACHIV_RAT": "1.0448"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.0448"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "강원",
            "ACHIV_RAT": "1.0477"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.0478"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.0523"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0530"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.0541"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "대전",
            "ACHIV_RAT": "1.0563"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.0612"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.0645"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0648"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "대전",
            "ACHIV_RAT": "1.0650"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0714"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0749"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0753"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.0856"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0902"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0950"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.0979"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.1071"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.1111"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.1117"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "광주",
            "ACHIV_RAT": "1.1154"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.1175"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.1367"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.1509"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.1577"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.1600"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.1760"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.1763"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.2086"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.2239"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.2650"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.2696"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.2789"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "경남",
            "ACHIV_RAT": "1.2824"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.2865"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.3297"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.3345"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.3522"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "경남",
            "ACHIV_RAT": "1.4302"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.6296"
        },
        {
            "WEEK_BEGIN_DT": "20221205",
            "WEEK_END_DT": "20221211",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "울산",
            "ACHIV_RAT": "1.7976"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.4674"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.6432"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.6594"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.6606"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.6718"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.6875"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.6906"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.6940"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.7180"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.7210"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.7213"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.7217"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.7234"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.7255"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.7272"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.7329"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.7371"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.7404"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.7408"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.7509"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.7697"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.7774"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.7833"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.7935"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.7950"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.7977"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8025"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.8058"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8071"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8138"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8153"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8154"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8198"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.8213"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.8218"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.8246"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.8274"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8279"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.8298"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8311"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.8362"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8423"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8442"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.8547"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8564"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8572"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.8583"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.8616"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.8617"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.8649"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8660"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.8663"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.8673"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8687"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.8704"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.8721"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.8735"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.8753"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.8760"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.8774"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.8787"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.8827"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.8830"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "충북",
            "ACHIV_RAT": "0.8834"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.8842"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.8884"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.8887"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.8907"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.8934"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.8961"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "제주",
            "ACHIV_RAT": "0.8982"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9018"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "충남",
            "ACHIV_RAT": "0.9020"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9048"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.9105"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9124"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9155"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "서울",
            "ACHIV_RAT": "0.9163"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "전북",
            "ACHIV_RAT": "0.9170"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9177"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.9181"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.9239"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "광주",
            "ACHIV_RAT": "0.9317"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9330"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.9346"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9470"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "서울",
            "ACHIV_RAT": "0.9471"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.9491"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9541"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "인천",
            "ACHIV_RAT": "0.9555"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.9566"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "서울",
            "ACHIV_RAT": "0.9622"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "세종",
            "ACHIV_RAT": "0.9634"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "울산",
            "ACHIV_RAT": "0.9647"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.9698"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "강원",
            "ACHIV_RAT": "0.9710"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9717"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9719"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9722"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9727"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "대구",
            "ACHIV_RAT": "0.9786"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "전남",
            "ACHIV_RAT": "0.9789"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "부산",
            "ACHIV_RAT": "0.9799"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9840"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "경북",
            "ACHIV_RAT": "0.9863"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "경기",
            "ACHIV_RAT": "0.9865"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "경남",
            "ACHIV_RAT": "0.9887"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "인천",
            "ACHIV_RAT": "0.9974"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "대전",
            "ACHIV_RAT": "0.9975"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0035"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.0045"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.0046"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.0047"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "전북",
            "ACHIV_RAT": "1.0057"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.0105"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.0120"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0127"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.0150"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.0153"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.0209"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "강원",
            "ACHIV_RAT": "1.0228"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "울산",
            "ACHIV_RAT": "1.0257"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.0257"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.0259"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0263"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0266"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0355"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.0407"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.0417"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.0434"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.0459"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.0464"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.0506"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.0512"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.0521"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "강원",
            "ACHIV_RAT": "1.0602"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0661"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "광주",
            "ACHIV_RAT": "1.0735"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0784"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0785"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.0820"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.0824"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "대전",
            "ACHIV_RAT": "1.0877"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "대전",
            "ACHIV_RAT": "1.0921"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "경기",
            "ACHIV_RAT": "1.0983"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.0990"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "3902",
            "GS_GD_SCLS_NM": "냉장커피",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.1007"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.1021"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.1157"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.1229"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "제주",
            "ACHIV_RAT": "1.1305"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.1322"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0901",
            "GS_GD_SCLS_NM": "일반빵",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.1436"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "전남",
            "ACHIV_RAT": "1.1496"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0905",
            "GS_GD_SCLS_NM": "상온디저트빵",
            "PVN_NM": "충북",
            "ACHIV_RAT": "1.1504"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "경남",
            "ACHIV_RAT": "1.1645"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "충남",
            "ACHIV_RAT": "1.1666"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.1676"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "6801",
            "GS_GD_SCLS_NM": "안전상비의약품",
            "PVN_NM": "경북",
            "ACHIV_RAT": "1.1894"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "세종",
            "ACHIV_RAT": "1.2215"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "0906",
            "GS_GD_SCLS_NM": "냉장디저트빵",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.2746"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "부산",
            "ACHIV_RAT": "1.2913"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "인천",
            "ACHIV_RAT": "1.2956"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "5601",
            "GS_GD_SCLS_NM": "초콜릿",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.3195"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "5021",
            "GS_GD_SCLS_NM": "수제맥주",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.3207"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "3901",
            "GS_GD_SCLS_NM": "가공우유",
            "PVN_NM": "서울",
            "ACHIV_RAT": "1.3340"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "경남",
            "ACHIV_RAT": "1.4154"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "대구",
            "ACHIV_RAT": "1.6204"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "7504",
            "GS_GD_SCLS_NM": "각티슈",
            "PVN_NM": "울산",
            "ACHIV_RAT": "2.5598"
        },
        {
            "WEEK_BEGIN_DT": "20221128",
            "WEEK_END_DT": "20221204",
            "GS_GD_SCLS_CD": "7401",
            "GS_GD_SCLS_NM": "바디보습류",
            "PVN_NM": "울산",
            "ACHIV_RAT": "3.6619"
        }
    ]