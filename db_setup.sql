/*
*  A file to setup the database for SimplePOS.
*  This file should be run once to setup the database.
*/

-- Create database simplepos if not exists
CREATE DATABASE IF NOT EXISTS simplepos;

-- Create user simplepos_usr with password simplepos_pwd if not exists
CREATE USER IF NOT EXISTS simplepos_usr IDENTIFIED BY 'simplepos_PWD';

-- Grant all privileges on simplepos DB to simplepos_usr
GRANT ALL PRIVILEGES ON simplepos.* TO simplepos_usr;

-- Flush privileges
FLUSH PRIVILEGES;
