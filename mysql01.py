import datetime
import random

import pymysql


def sql01():
    conn = pymysql.connect(
        host='db-001.lvpuhui.com',
        port=3306,
        user='root',
        password='Root_123',
        database='chain_carbon')

    start_date = datetime.date(2023, 12, 23)
    end_date = datetime.date(2024, 1, 10)
    cursor = conn.cursor()
    while start_date <= end_date:
        formatted_date = start_date.strftime("%Y%m%d")
        add_user = random.randint(1, 10)
        emission_sum_tmp = random.uniform(222261738, 322261738)
        emission_sum = "%.2f" % emission_sum_tmp
        points_grant = random.randint(200, 300)
        emission_points = random.randint(1000, 4000)
        activity_points = random.randint(1000, 4000)
        emission_user_number = random.randint(10000, 40000)
        emission_number = random.randint(40000, 70000)
        expend_points = random.randint(100, 200)
        sql = "INSERT INTO chain_carbon.gl_statistics_day_chart " \
              "(add_user, emission_sum, points_grant, emission_points, activity_points, emission_user_number, emission_number, expend_points, statistics_time) " \
              "VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {});".format(add_user, emission_sum, points_grant,
                                                                    emission_points, activity_points,
                                                                    emission_user_number,
                                                                    emission_number, expend_points, formatted_date)
        print(sql)
        start_date += datetime.timedelta(days=1)
        cursor.execute(sql)
        conn.commit()
    cursor.close()
    conn.close()


def sql02():
    conn = pymysql.connect(
        host='db-001.lvpuhui.com',
        port=3306,
        user='root',
        password='Root_123',
        database='chain_carbon')
    cursor = conn.cursor()
    for i in range(20):
        sql = "INSERT INTO chain_carbon.gl_chain_config (app_name, app_id, scenario_id, status, deleted) VALUES ('应用01', 'zmVm9lqI', 8, 1, 0);"
        cursor.execute(sql)
        conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    # sql01()
    sql02()
