package org.jihyeong.controller;


import java.util.List;

import org.jihyeong.domain.Criteria;
import org.jihyeong.domain.ReplyVO;
import org.jihyeong.service.BoardService;
import org.jihyeong.service.ReplyService;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import lombok.AllArgsConstructor;
import lombok.extern.log4j.Log4j;

@Controller
@Log4j
@RequestMapping("/replies")
@AllArgsConstructor
public class ReplyController {
	private ReplyService service;
	
	//등록
	@PostMapping(value="/new", 
	consumes="application/json",
	produces= {MediaType.TEXT_PLAIN_VALUE})
	public ResponseEntity<String> create(@RequestBody ReplyVO vo) {
		log.info("ReplyVO: " + vo);
		int insertCount = service.register(vo);
		log.info("Reply Insert count : " + insertCount);
		return insertCount==1
		? new ResponseEntity<>("success", HttpStatus.OK)
		:new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
	}
	
	@GetMapping(value="/pages/{bno}/{page}",
	produces= 
	{MediaType.APPLICATION_XML_VALUE,MediaType.APPLICATION_JSON_VALUE})
	public ResponseEntity<List<ReplyVO>> getList(
			@PathVariable("page")int page,
			@PathVariable("bno")Long bno){
		log.info("getList..............");
		Criteria cri = new Criteria(page, 5);
		log.info("cri :" + cri);
		return new ResponseEntity<> (service.getList(cri, bno), HttpStatus.OK);
	}
	
	@GetMapping(value="/{rno}",
	produces= {MediaType.APPLICATION_XML_VALUE,
	MediaType.APPLICATION_JSON_VALUE})
	public ResponseEntity<ReplyVO> get(@PathVariable("rno")Long rno){
		log.info("get:" + rno);
		return new ResponseEntity<>(service.get(rno),HttpStatus.OK);
	}
	
	@DeleteMapping(value="/{rno}", produces= {MediaType.TEXT_PLAIN_VALUE})
	public ResponseEntity<String> remove(@PathVariable("rno")Long rno){
		log.info("remove:"+rno);
		return service.remove(rno)==1
		? new ResponseEntity<>("success", HttpStatus.OK)
		:new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);
	}
	
	@RequestMapping(method={RequestMethod.PUT, RequestMethod.PATCH},
		value="/{rno}",
		consumes="application/json",
		produces= {MediaType.TEXT_PLAIN_VALUE})
		public ResponseEntity<String>modify(@RequestBody ReplyVO vo, @PathVariable("rno")Long rno){
			vo.setRno(rno);
			log.info("rno:"+rno);
			log.info("modify:"+vo);
			return service.modify(vo)==1
			? new ResponseEntity<>("success", HttpStatus.OK)
			:new ResponseEntity<>(HttpStatus.INTERNAL_SERVER_ERROR);	
	}
}
