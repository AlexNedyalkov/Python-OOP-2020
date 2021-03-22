#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 10:19:02 2020

@author: user
"""

'''
    5. Programmer
Create a class called Programmer. Upon initialization it should receive name (string),
language (string), skills (integer). The class should have two methods:
    • watch_course(course_name, language, skills_earned)
        ◦ If the programmer's language is the equal to the one on the course 
        increase his skills with the given one and 
        return a message "{programmer} watched {course_name}".
        ◦ Otherwise return "{name} does not know {language}".
    • change_language(new_language, skills_needed) 
        ◦ If the programmer has the skills and
        the language is different from his,
        change his language to the new one and return "{name} switched from {previous_language} to {new_language}".
        ◦ If the programmer has the skills, but the language is the same as his return "{name} already knows {language}".
        ◦ In the last case the programmer does not have the skills, so return "{name} needs {needed_skills} more skills" and don't change his language
'''

class Programmer:
    
    def __init__(self, name, language, skills):
        
        self.name = name
        self.language = language
        self.skills = skills
        
    def watch_course(self, course_name, language, skills_earned):
        
        if course_name == self.language:
            self.skills += skills_earned
            return f"{self.programmer} watched {course_name}"
        else:
            return f"{self.name} does not know {language}"
    
    def change_language(self, new_langauge, skills_needed):
        
         if self.skills >= skills_needed and new_language != self.language:
             self.language = new-language
             return f"{name} switched from {previous_language} to {new_language}"