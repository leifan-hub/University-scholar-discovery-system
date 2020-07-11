package com.ssm.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import com.ssm.domain.Expert;
import com.ssm.service.ExpertService;

@Controller
@RequestMapping("expert")
public class ExpertController {

	@Autowired
	private ExpertService expertService;
	
	@RequestMapping("/getExpertList")
	public ModelAndView getUserList() {
		List<Expert> expertList = expertService.getExpertList();
		
		ModelAndView model = new ModelAndView();
		model.addObject("expertList", expertList);
		model.setViewName("expertDetail");
		return model;
	}
	
	@RequestMapping("/returnIndex")
	public ModelAndView returnIndex() {
		List<Expert> expertList = expertService.getExpertList();
		
		ModelAndView model = new ModelAndView();
		model.addObject("expertList", expertList);
		model.setViewName("index");
		return model;		
	}
	
	@RequestMapping("/getExpertByName")
	public ModelAndView getExpertByName(String name) {
		List<Expert> expert =expertService.getExpertByName(name);
		
		ModelAndView model = new ModelAndView();
		model.addObject("expertList", expert);
		model.setViewName("expertDetail");
		return model;
	}
	
	@RequestMapping("/getExpertBySchool")
	public ModelAndView getExpertBySchool(String school) {
		List<Expert> expert =expertService.getExpertBySchool(school);
		
		ModelAndView model = new ModelAndView();
		model.addObject("expertList", expert);
		model.setViewName("expertDetail");
		return model;
	}
	
	@RequestMapping("/getExpertByMajor")
	public ModelAndView getExpertByMajor(String major) {
		List<Expert> expert =expertService.getExpertByMajor(major);
		
		ModelAndView model = new ModelAndView();
		model.addObject("expertList", expert);
		model.setViewName("expertDetail");
		return model;
	}	
	
	@RequestMapping("/getExpertBySubject")
	public ModelAndView getExpertBySubject(String subject) {
		List<Expert> expert =expertService.getExpertBySubject(subject);
		
		ModelAndView model = new ModelAndView();
		model.addObject("expertList", expert);
		model.setViewName("expertDetail");
		return model;
	}	
	
	@RequestMapping("/getExpertByPaper")
	public ModelAndView getExpertByPaper(String paper) {
		List<Expert> expert =expertService.getExpertByPaper(paper);
		
		ModelAndView model = new ModelAndView();
		model.addObject("expertList", expert);
		model.setViewName("expertDetail");
		return model;
	}	
	
	@RequestMapping("/getExpertByResearch")
	public ModelAndView getExpertByResearch(String research_direction) {
		List<Expert> expert =expertService.getExpertByResearch(research_direction);
		
		ModelAndView model = new ModelAndView();
		model.addObject("expertList", expert);
		model.setViewName("expertDetail");
		return model;
	}	
	
	@RequestMapping("/getExpertByIntroduction")
	public ModelAndView getExpertByIntroduction(String introduction) {
		List<Expert> expert =expertService.getExpertByIntroduction(introduction);
		
		ModelAndView model = new ModelAndView();
		model.addObject("expertList", expert);
		model.setViewName("expertDetail");
		return model;
	}	

	@RequestMapping("/getExpertById")
	public ModelAndView getExpertById(int id) {
		Expert expert =expertService.getExpertById(id);
		
		ModelAndView model = new ModelAndView();
		model.addObject("expert", expert);
		model.setViewName("expertDetail");
		return model;
	}	

	@RequestMapping("/index")
	public ModelAndView index() {
		List<Expert> expertList = expertService.getExpertList();
		
		ModelAndView model = new ModelAndView();
		model.addObject("expertList", expertList);
		model.setViewName("index");
		return model;
	}
	
	@RequestMapping("/delete")
	public ModelAndView delete(int id) {
		expertService.delete(id);
		List<Expert> expertList = expertService.getExpertList();
		
		ModelAndView model = new ModelAndView();
		model.addObject("expertList", expertList);
		model.setViewName("index");
		return model;
	}	

	@RequestMapping("/preaddExpert")
	public ModelAndView preaddExpert() {
		ModelAndView model = new ModelAndView();
		model.setViewName("addExpert");
		return model;
	}
	
	@RequestMapping("/addExpert")
	public ModelAndView addExpert(Expert expert) {
		expertService.addExpert(expert);		
		
		List<Expert> expertList = expertService.getExpertList();
		
		ModelAndView model = new ModelAndView();
		model.addObject("expertList", expertList);
		model.setViewName("index");
		return model;
	}
	
	@RequestMapping("/preupdate")
	public ModelAndView preupdate(int id) {
		ModelAndView model=new ModelAndView();
		model.addObject("expert", expertService.getExpertById(id));
		model.setViewName("update");
		return model;
	}
	
	
	@RequestMapping("/update")
	public ModelAndView update(Expert expert) {
		expertService.update(expert);		
		
		List<Expert> expertList = expertService.getExpertList();
		
		ModelAndView model = new ModelAndView();
		model.addObject("expertList", expertList);
		model.setViewName("index");
		return model;	
	}
	
	
}