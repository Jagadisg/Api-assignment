from sql import get_users_conn

def get_users_by_company(company_id):
    cursor = ucon.cursor()
    cursor.execute(f"SELECT * FROM user_detail WHERE companyId = {company_id}")
    users = cursor.fetchall()
    return users

ucon=get_users_conn()
company_id = 2  # Change this to the desired companyId
users = get_users_by_company(company_id)
print("sql assignment output by company id :",company_id)
print(users)
