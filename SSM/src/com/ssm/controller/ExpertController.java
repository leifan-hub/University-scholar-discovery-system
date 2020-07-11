package com.ssm.controller;


import java.util.ArrayList;
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
		model.setViewName("expert");
		return model;
	}
	
	@RequestMapping("/getExpertByName")
	public ModelAndView getExpertByName(String name) {
		List<Expert> expert =expertService.getExpertByName(name);
		String direction = expert.get(0).getResearch_direction();
		List<Expert> expertrelated = expertService.getExpertByResearch_direction(direction);
		for(int i=0;i<expertrelated.size();i++) {
			if(expertrelated.get(i).getId()==expert.get(0).getId()) {
				expertrelated.remove(i);
			}
		}
		ModelAndView model = new ModelAndView();
		model.addObject("expertList", expert);
		model.addObject("expertrelatedList", expertrelated);
		model.setViewName("expert");
		return model;
	}
	@RequestMapping("/getExpertById")
	public ModelAndView getExpertById(int id) {
		List<Expert> expert = new ArrayList();
		expert.add(expertService.getExpertById(id));
		String direction = expert.get(0).getResearch_direction();
		List<Expert> expertrelated = expertService.getExpertByResearch_direction(direction);
		for(int i=0;i<expertrelated.size();i++) {
			if(expertrelated.get(i).getId()==expert.get(0).getId()) {
				expertrelated.remove(i);
			}
		}
		ModelAndView model = new ModelAndView();
		model.addObject("expertList", expert);
		model.addObject("expertrelatedList", expertrelated);
		model.setViewName("expert");
		return model;
	}
	
	
	
	@RequestMapping("/index")
	public ModelAndView index() {
		ModelAndView model = new ModelAndView();
		
		model.setViewName("index");
		return  model;
	}
	
	@RequestMapping("/delete")
	public ModelAndView delete(int id) {
		expertService.delete(id);
		return new ModelAndView("redirect:/expert/index");
	}
	
	
	
	@RequestMapping("/returnIndex")
	public ModelAndView returnIndex() {
		
		return new ModelAndView("redirect:/expert/index");
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
		
		return new ModelAndView("redirect:/expert/index"); 
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
		
		return new ModelAndView("redirect:/expert/getExpertList");
	
	}
	@RequestMapping("/expertDetail")
	public ModelAndView expertDetail() {
		ModelAndView model=new ModelAndView();
		
		model.setViewName("expertDetail");
		return model;
	
	}
	
}