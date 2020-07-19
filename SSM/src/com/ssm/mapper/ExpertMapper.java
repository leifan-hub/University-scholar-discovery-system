package com.ssm.mapper;
/**
* author£ººúÖ¾ºÀ ÀîÁú¾ü À×·²
* create: time: 2020-07-05
* update£ºtime:  2020-07-18
*/
import java.util.List;

import org.springframework.web.servlet.ModelAndView;

import com.ssm.domain.Countclass;
import com.ssm.domain.Expert;


public interface ExpertMapper {
	public List<Countclass> countnums();
	public List<Expert> getExpertList();
	public List<Expert> getExpertByName(String name);
	public List<Expert> getExpertBySchool(String school);
	public List<Expert> getExpertByMajor(String major);
	public List<Expert> getExpertBySubject(String subject);
	public List<Expert> getExpertByPaper(String paper);
	public List<Expert> getExpertByResearch(String research_direction);
	public List<Expert> getExpertByIntroduction(String introduction);
	public Expert getExpertById(int id);
	public int addpageview(int id);
	public String getExpertPicByName(String name);
	public String getExpertTagByName(String name);
}
