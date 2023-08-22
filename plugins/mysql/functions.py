import json
import os
import mysql.connector

async def execute_sql_query(sql_query: str, is_save: bool, save_file_name: str = "sql_query_result.json"):
    """
    Execute a SQL query and return the results.you can only use the test_sql database

    Parameters:
        sql_query: The SQL query to execute. (required)
        is_save: Whether to save the result to a file. if the result is big, it is recommended to set it to True. (required)
        save_file_name: The name of the file to save the result. (default: sql_query_result.json)
    """
    # Load database configuration from config.json
    # 获取本文件夹下的config.json文件中的内容
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path) as config_file:
        config = json.load(config_file)
        
    db_config = {k: config[k] for k in ['user', 'password', 'host', 'database'] if k in config}

    # Connect to the MySQL server
    cnx = mysql.connector.connect(**db_config)
    try:
        # Create a cursor object
        cursor = cnx.cursor()

        # Execute the SQL query
        cursor.execute(sql_query)

        # Fetch all the rows
        rows = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        cnx.close()

        # Return the results
        print(rows)
        if is_save:
            with open(save_file_name, "w") as f:
                json.dump(rows, f)
            return {
                "result": f"Result saved to {save_file_name}",
                "sql_ip": db_config["host"],
                "sql_user": db_config["user"],
                "sql_database": db_config["database"],
            }
        else:
            return {
                "result": rows,
                "sql_ip": db_config["host"],
                "sql_user": db_config["user"],
                "sql_database": db_config["database"],
                "sql_password": db_config["password"]
            }
    except Exception as e:
        return {
            "error": str(e),
            "sql_ip": db_config["host"],
            "sql_user": db_config["user"],
            "sql_database": db_config["database"],
            "sql_password": db_config["password"]
        }