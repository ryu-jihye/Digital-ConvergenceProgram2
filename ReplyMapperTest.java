package org.jihyeong.sample;

import java.util.List;
import java.util.stream.IntStream;

import org.jihyeong.domain.Criteria;
import org.jihyeong.domain.ReplyVO;
import org.jihyeong.mapper.ReplyMapper;
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
public class ReplyMapperTest {
	@Setter(onMethod = @__({@Autowired}))
	private ReplyMapper mapper;
	
	@Test
	public void testMapper() { //mapper오휴 시 위의 setter 부분의 mapper선언 되었는지 확인하기
		log.info(mapper);
	}
	
	private Long[] bnoArr = {32L, 33L, 34L, 35L, 36L};
	//기존 bno 내 숫자 이용
	
	@Test
	public void testCreate() {
		IntStream.rangeClosed(1, 10).forEach(i-> {
			ReplyVO vo = new ReplyVO();
			vo.setBno(bnoArr[i % 5]);
			vo.setReply("댓글 테스트  " + i);
			vo.setReplyer("replyer" + i);
			mapper.insert(vo);
		});
	}
	
	@Test
	public void testRead() {
		Long targetRno = 5L;
		ReplyVO vo = mapper.read(targetRno); log.info(vo);
	}
	
	@Test
	public void testDelete() {
		Long targetRno = 10L;
		mapper.delete(targetRno);
	}
	
	@Test
	public void testUpdate(){
		Long targetRno = 11L;
		ReplyVO vo = mapper.read(targetRno);
		vo.setReply("Update Reply");
		/* vo.setReplyer("update 작성자"); */
		int count = mapper.update(vo);
		log.info("Update Count :" + count);
	}
	
	@Test
	public void testList() {
		Criteria cri = new Criteria();
		List<ReplyVO> replies = 
				mapper.getListWithPaging(cri, bnoArr[0]);
		replies.forEach(reply->log.info(reply));
	}
	@Test
	public void testList2() {
		Criteria cri = new Criteria(2, 5);
		List<ReplyVO> replies = mapper.getListWithPaging(cri, 50L);
		replies.forEach(reply->log.info(reply));
	}
}
