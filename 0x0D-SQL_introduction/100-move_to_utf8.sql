-- Converts the hbtn_0c_0 database to use UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Use the hbtn_0c_0 database for subsequent operations
USE hbtn_0c_0;

-- Converts the first_table table to use UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Converts the `name` field in the first_table to use UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
ALTER TABLE first_table MODIFY COLUMN name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

