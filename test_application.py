import pytest
import sqlite3
from application import loginCheck,settingCode


def query():
    conn=None
    try:
        conn=sqlite3.connect("login.db")
    except Exception as e:
        print("error connecting")
    cur=conn.cursor()
    cur.execute("SELECT TASK FROM PROGRESS WHERE USERNAME='test'")
    result=cur.fetchall()
    return result

def test_login_match():
    foundMatch=loginCheck("test","testpassword")
    assert foundMatch==True
def test_login_not_match():
    foundMatch=loginCheck("test","fakepassword")
    assert foundMatch==False
def test_login_fake_username():
    foundMatch=loginCheck("wrong","fakepassword")
    assert foundMatch==False
def test_login_fake_password():
    foundMatch=loginCheck("test","wrong")
    assert foundMatch==False
def test_login_nonmatch():
    foundMatch=loginCheck("wrong","madeup")
    assert foundMatch==False

def test_code_enable_teacher_mode():
    settingCode("teacher")
    result=query()
    print(result)
    assert result[0]==18
def test_code_disable_teacher_mode():
    settingCode("notTeacher")
    result=query()
    assert result[0]==1
def test_code_unlock_tasks():
    settingCode("5")
    result=query()
    assert result[0]==5
def test_code_incorrect():
    start=query()
    settingCode("wrong")
    result=query()
    assert result[0]==start[0]
def test_code_empty():
    start=query()
    settingCode("")
    result=query()
    assert result[0]==start[0]