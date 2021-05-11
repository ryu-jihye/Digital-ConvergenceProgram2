package org.kcm.mapper;

import java.util.List;

import org.apache.ibatis.annotations.Select;
import org.kcm.domain.BoardVO;

public interface BoardMapper {

	/* @Select("select * from tbl_board where bno > 0") */
	public List<BoardVO> getList();
	
	//BoardMapperTest 사용 시 반드시 필요
	public void insert(BoardVO board); 
	
	public void insertSelectKey(BoardVO board);
	
	public BoardVO read(Long bno);
	
	public int delete (Long bno);
	public int update(BoardVO board);
}

