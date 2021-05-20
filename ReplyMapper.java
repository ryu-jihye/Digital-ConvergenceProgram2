package org.jihyeong.mapper;

import java.util.List;

import org.apache.ibatis.annotations.Param;
import org.jihyeong.domain.Criteria;
import org.jihyeong.domain.ReplyVO;

public interface ReplyMapper {
	public int insert(ReplyVO vo);
	
	public ReplyVO read(Long rno);
	
	public int delete(Long rno);
	
	public int update(ReplyVO reply);
	
	public List<ReplyVO> getListWithPaging(
			//Param 이용 이유 : myBatis패러미터는 1개만 허용하기에
			//2개이상 전달 위해 @Param 이용 -> #{}사용 가능
			@Param("cri") Criteria cri,
			@Param("bno") Long bnoArr);
	
	public int getCountByBno (Long bno);

}
