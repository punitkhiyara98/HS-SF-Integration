#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created by: Punit & Stephen 
Date Created: 4/7/2020
'''

import PrivateKeys as fetchkeys
import pandas as pd
import Functions as custfunc
import requests
import DBconnection as connection

url, authHeader = fetchkeys.access_variables()  # function call to fetch the url, authHeader, api key and auth token
env_type = fetchkeys.env_select()  # function call to fetch the environment of run.

# CONNECT TO DATABASE SERVER
# DB Connection Setup
mydb, mySchema = connection.getDatabaseConnectionDev()
mycursor = mydb.cursor()

mycursor.execute(
    "SELECT detailed_name, detailed_id, consolidated_name, consolidated_id, default_value FROM " + mySchema +
    ".industry_lookup;")

companies = custfunc.getAllCompanies(url, authHeader)
type(companies)