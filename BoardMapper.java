package org.conan.mapper;

import java.util.List;

import org.apache.ibatis.annotations.Select;
import org.conan.domain.BoardVO;

public interface BoardMapper { //tbl_bbs 사용(기존 tbl_board)
	/* @Select("select * from tbl_bbs where bno>0") */
	public List<BoardVO> getList();
	
	public void insert(BoardVO board);
	
	public void insertSelectKey(BoardVO board);
	
	public BoardVO read(Long bno);
	//bno를 참조해서 삭제하는데 bno를 쓰니까 long타입으로
	public int delete(Long bno);
	
	public int update(BoardVO board);
}
