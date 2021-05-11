package org.kcm.sample;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.kcm.domain.BoardVO;
import org.kcm.mapper.BoardMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

import lombok.Setter;
import lombok.extern.log4j.Log4j;

@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration("file:src/main/webapp/WEB-INF/spring/root-context.xml")
@Log4j
public class BoardMapperTest { //전체 내용 나옴
	@Setter(onMethod = @__({@Autowired}))
	private BoardMapper mapper;
	
	@Test //전체 내용 나옴
	public void testGetList() {
			mapper.getList().forEach(board->log.info(board)); //람다식 표현
		}
	
	@Test
	public void testInsert() { //새로운 내용 추가
		BoardVO board = new BoardVO();
		board.setTitle("새로 작성하는 글");
		board.setContent("새로 작성하는 내용");
		board.setWriter("newbie");
		mapper.insert(board);
		log.info(board);
	}
	@Test 
	public void testRead() { //게시물 조회(번호에 따라 조회하는 내용이 달라짐)
		BoardVO board = mapper.read(6L);
		log.info(board);
	}
	@Test
	public void testDelete() {//게시글 삭제
		log.info("DELETE COUNT: " + mapper.delete(5L));
	}
	@Test
	public void testUpdate() {//게시글 수정하기
		BoardVO board = new BoardVO();
		board.setBno(2L);
		board.setTitle("수정한 제목");
		board.setContent("수정한 내용");
		board.setWriter("rose");
		int count = mapper.update(board);
		log.info("UPDATE COUNT : " + count);
	}
	
}