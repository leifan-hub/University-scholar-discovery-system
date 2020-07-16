package com.ssm.controller;
import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import com.ssm.domain.Expert;
import com.ssm.service.ExpertService;
/**
* author£ººúÖ¾ºÀ ÀîÁú¾ü À×·² Í¿çìçâ
* create: time: 2020-07-05
* update£ºtime:  2020-07-12
*/
@Controller
@RequestMapping("expert")
public class ExpertController {

	@Autowired
	private ExpertService expertService;
	
//	@RequestMapping("/getExpertList")
//	public ModelAndView getUserList() {
//		List<Expert> expertList = expertService.getExpertList();
//		
//		ModelAndView model = new ModelAndView();
//		model.addObject("expertList", expertList);
//		model.setViewName("expertDetail");
//		return model;
//	}
	
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
		model.setViewName("queryExpertName");
		return model;
	}
	
	@RequestMapping("/getExpertBySchool")
	public ModelAndView getExpertBySchool(String school) {
		List<Expert> expert =expertService.getExpertBySchool(school);
		
		ModelAndView model = new ModelAndView();
		model.addObject("expertList", expert);
		model.setViewName("queryExpertSchool");
		return model;
	}
	
	@RequestMapping("/getExpertByMajor")
	public ModelAndView getExpertByMajor(String major) {
		List<Expert> expert =expertService.getExpertByMajor(major);
		
		ModelAndView model = new ModelAndView();
		model.addObject("expertList", expert);
		model.setViewName("queryExpertMajor");
		return model;
	}	
	
	@RequestMapping("/getExpertBySubject")
	public ModelAndView getExpertBySubject(String subject) {
		List<Expert> expert =expertService.getExpertBySubject(subject);
		
		ModelAndView model = new ModelAndView();
		model.addObject("expertList", expert);
		model.setViewName("queryExpertSubject");
		return model;
	}	
	
	@RequestMapping("/getExpertByPaper")
	public ModelAndView getExpertByPaper(String paper) {
		List<Expert> expert =expertService.getExpertByPaper(paper);
		
		ModelAndView model = new ModelAndView();
		model.addObject("expertList", expert);
		model.setViewName("queryExpertPaper");
		return model;
	}	
	
	@RequestMapping("/getExpertByResearchDirection")
	public ModelAndView getExpertByResearch(String research_direction) {
		List<Expert> expert =expertService.getExpertByResearch(research_direction);
		
		ModelAndView model = new ModelAndView();
		model.addObject("expertList", expert);
		model.setViewName("queryExpertDirection");
		return model;
	}	
	
	//@RequestMapping("/getExpertByIntroduction")
	//public ModelAndView getExpertByIntroduction(String introduction) {
	//	List<Expert> expert =expertService.getExpertByIntroduction(introduction);
		
	//	ModelAndView model = new ModelAndView();
	//	model.addObject("expertList", expert);
	//	model.setViewName("expertDetail");
	//	return model;
//	}	

	@RequestMapping("/getExpertById")
	public ModelAndView getExpertById(int id) {
		Expert expert =expertService.getExpertById(id);
		expertService.addpageview(id);
		List<String>expertPapers=new ArrayList<String>();
		List<String>expertDirections=new ArrayList<String>();
		
		String[] expertPapers_string=expert.getPaper().split("#");
		for (String expertPaper : expertPapers_string) {
			expertPapers.add(expertPaper);
		}
		
		String[] expertDirections_string=expert.getResearch_direction().split(",|¡£|¡¢");
		for (String expertDirection : expertDirections_string) {
			expertDirections.add(expertDirection);
			System.out.println(expertDirection);
		}
		String Research=expert.getResearch_direction();
		List<Expert> expertrelated =expertService.getExpertByResearch(Research);
		for(int i=0;i<expertrelated.size();i++) {
			if(expertrelated.get(i).getId()==expert.getId()) {
				expertrelated.remove(i);
			}
		}
		ModelAndView model = new ModelAndView();
		model.addObject("expert", expert);
		model.addObject("expertrelatedList", expertrelated);
		model.addObject("expertPapers", expertPapers);
		model.addObject("expertDirections", expertDirections);
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