package com.ssm.service.impl;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;

import com.ssm.domain.Expert;
import com.ssm.mapper.ExpertMapper;
import com.ssm.service.ExpertService;

public class ExpertServiceImpl implements ExpertService {

	@Autowired
	private ExpertMapper expertMapper;

	
	@Override
	public List<Expert> getExpertList() {
		
		return expertMapper.getExpertList();
	}
	public List<Expert> getExpertByName(String name){
		
	return expertMapper.getExpertByName(name);
	}
	
	public List<Expert> getExpertBySchool(String school){
		
	return expertMapper.getExpertBySchool(school);
	}
	
	public List<Expert> getExpertByMajor(String major){
		
	return expertMapper.getExpertByMajor(major);
	}
	
	public List<Expert> getExpertBySubject(String subject){
		
	return expertMapper.getExpertBySubject(subject);
	}
	
	public List<Expert> getExpertByPaper(String paper){
		
	return expertMapper.getExpertByPaper(paper);
	}
	
	public List<Expert> getExpertByResearchDirection(String research_direction){
		
	return expertMapper.getExpertByResearchDirection(research_direction);
	}
	
	public Expert getExpertById(int id) {
		return expertMapper.getExpertById(id);
		
	}
	public int addExpert(Expert expert) {
		
		return expertMapper.addExpert(expert);
	}
	
    public int update(Expert expert) {
				
    	return  expertMapper.update(expert);
	}
	
	public int delete(int id) {
		return expertMapper.delete(id);
	}
	
	
}
