package org.conan.sample;

import org.conan.domain.BoardVO;
import org.conan.mapper.BoardMapper;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

import lombok.Setter;
import lombok.extern.log4j.Log4j;

@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration("file:src/main/webapp/WEB-INF/spring/root-context.xml")
@Log4j
public class BoardMapperTest {
	@Setter(onMethod = @__({@Autowired}))
	private BoardMapper mapper;
	@Test
	public void testGetList() {
		//람다식 표현
		mapper.getList().forEach(board->log.info(board));
	}
	@Test
	public void testInsert(){
		BoardVO board = new BoardVO();
		board.setTitle("새로 작성하는 글");
		board.setContent("새로 작성하는 내용");
		board.setWriter("newbie");
		mapper.insert(board);
		log.info(board);
	}
	@Test
	public void testRead() {
		BoardVO board = mapper.read(5L);
		log.info(board);
	}

	@Test
	public void testDelete() {
		log.info("DELETE COUNT: "+mapper.delete(5L));
	}
	@Test
	public void testUpdate(){
		BoardVO board = new BoardVO();
		board.setBno(2L);
		board.setTitle("수정하는 글");
		board.setContent("수정하는 내용");
		int count = mapper.update(board);
		log.info("UPDATE COUNT : " + count);
	}
}
