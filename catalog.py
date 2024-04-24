# Tables Module
import psycopg2

def admin_auth(config, usern, passw) :
    """Creates catalog table - only created when admin logs in before user."""
    cmds = (
        # cmds[0] - Check if user is an admin
        # User-defined role "admin" has schema permission to create tables
        """
        SELECT pg_catalog.has_schema_privilege(current_user, current_schema, 'CREATE') as "create";
        """,
        # cmds[1] - Create table of shop catalog
        """
        CREATE TABLE IF NOT EXISTS shop(
            item_id SERIAL PRIMARY KEY,
            item_name VARCHAR(255) NOT NULL,
            item_price DECIMAL(7,2) NOT NULL,
            cat_id VARCHAR(127) NOT NULL,
            quantity INTEGER CHECK (quantity >= 0) NOT NULL
        )
        """,
        # cmds[2] - Delete table in case of any emergency
        """
        DROP TABLE shop;
        """
        )

    try:
        with psycopg2.connect(
            **config,
            user = usern,
            password = passw
        ) as conn:
            cur = conn.cursor()

            # cur.execute(cmds[2])
            cur.execute(cmds[0])
            isAdmin = cur.fetchone()

            if isAdmin[0] == True:
                cur.execute(cmds[1])
                cur.close()
                return True
            else:
                cur.close()
                return False

    except (psycopg2.DatabaseError, Exception) as error:
        # print(error)
        print(error)