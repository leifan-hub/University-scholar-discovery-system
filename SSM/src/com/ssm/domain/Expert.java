package com.ssm.domain;
/**
* author����־�� 
* create: time: 2020-07-05
* update��time:  2020-07-12
*/
public class Expert {
 private int id;
 private String name;
 private String school;
 private String major;
 private String subject;
 private String paper;
 private String research_direction;
 private String introduction;
 private int pageview;
 public int getId() {
	 return id;
 }
 public void setId(int id){
	 this.id=id;
 }
 public String getName() {
	 return name;
 }
 public void setName(String name) {
	 this.name=name;
 }
 public String getSchool() {
	 return school;
 }
 public void setSchool(String school) {
	 this.school=school;
 }
 public String getMajor() {
	 return major;
 }
 public void setMajor(String major) {
	 this.major=major;
 }
 public String getSubject() {
	 return subject;
 }
 public void setSubject(String subject) {
	 this.subject=subject;
 }
 public String getPaper() {
	 return paper;
 }
 public void setPaper(String paper) {
	 this.paper=paper;
 }
 public String getResearch_direction() {
	 return research_direction;
 }
 public void setResearch_direction(String research_direction) {
	 this.research_direction=research_direction;
 }
 public String getIntroduction() {
	 return introduction;
 }
 public void setIntroduction(String introduction) {
	 this.introduction=introduction;
 }
 public int getPageview() {
	 return pageview;
 }
 public void setPageview(int pageview) {
	 this.pageview=pageview;
 }
 
}
