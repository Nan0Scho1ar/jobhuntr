#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
import datetime
import warnings

def indeed_bot(job_title, location, num_jobs):
    # Selenium Setup
    driver = webdriver.Firefox()
    # driver.get('https://secure.indeed.com/account/login')
    # #Begin
    # print("Logging in...")
    # driver.find_element_by_id('login-email-input').send_keys(USERNAME)
    # driver.find_element_by_id('login-password-input').send_keys(PASSWORD)
    # input("Press enter once login complete")
    driver.get('https://au.indeed.com/')
    print(f"Beginning search for quick apply {job_title} jobs in {location}.")
    driver.find_element_by_id('text-input-what').send_keys(job_title)
    driver.find_element_by_id('text-input-where').send_keys(location + Keys.RETURN)
    time.sleep(5)
    jobnum = 0
    page = 1
    while jobnum < num_jobs:
        quick_apply = driver.find_elements_by_class_name("indeedApply")
        for job in quick_apply:
            if jobnum > num_jobs:
                break
            job.click()
            jobnum += 1
            print(f"found {jobnum} Jobs.")
        if jobnum > num_jobs:
            break
        page += 1
        print(f"Navigating to page {page}")
        pagination = driver.find_element_by_class_name("pagination-list")
        pages = pagination.find_elements_by_tag_name("li")
        pages[-1].click()
        time.sleep(3)
        try:
            driver.find_element_by_class_name("popover-x-button-close").click()
            time.sleep(0.5)
        except:
            print("no popup")
    print("Here is a list of jobs:\n")
    #driver.close() #Close search tab
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        print(driver.current_url)

def cenniebot(fname):
    driver = webdriver.Firefox()
    driver.get('https://jobsearch.gov.au/jobseekers/my-job-search-effort')
    time.sleep(5)
    input("Press enter once login complete")
    today = datetime.date.today()
    jobnum = 1
    with open(fname, "r") as f:
        for line in f.readlines():
            print("Entering info for job " + str(jobnum))
            fields = [l.strip() for l in line.split(" | ")]
            driver.find_element_by_id('AddExternalJob-Btn').click()
            driver.find_element_by_id('ApplicationSentDate').send_keys(today.strftime("%d/%m/%Y"))
            driver.find_element_by_id('JobTitle').send_keys(fields[0])
            driver.find_element_by_id('AgentName').send_keys(fields[1])
            driver.find_element_by_id('JobLocation').send_keys(fields[2])
            driver.find_element_by_id('EmployerContact').send_keys("Indeed")
            driver.find_element_by_id('ApplicationMethod').send_keys("Online")
            save = driver.find_element_by_class_name('formsave')
            # Need to add extra click for reengagement
            # save = driver.find_element_by_class_name('fa-save')
            # input("Press enter to continue")
            save.click()
            time.sleep(1)
            save.click()
            time.sleep(5)
            jobnum += 1

warnings.filterwarnings('ignore')
bot = input("1: CennieBot\n2: IndeedBot\n> ")
if bot == "1":
    print("Starting CennieBot")
    path = input("Enter file path: ")
    cenniebot(path)
elif bot == "2":
    print("Starting indeedbot")
    job_title = input("Enter job title: ")
    location = input("Enter location: ")
    num_jobs = int(input("Enter num jobs: "))
    indeed_bot(job_title, location, num_jobs)
