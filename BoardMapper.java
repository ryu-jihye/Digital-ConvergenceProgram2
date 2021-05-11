package org.conan.mapper;

import java.util.List;

/*import org.apache.ibatis.annotations.Select;*/
import org.conan.domain.BoardVO;

public interface BoardMapper {
   /* @Select("select * from tbl_board where bno>0") */
   //목록으로 가져옴
   public List<BoardVO> getList();
   //생선된 PK값을 알 필요가 없는 경우
   public void insert(BoardVO board);
   //생성된 PK값을 알아야하는 경우
   public void insertSelectKey(BoardVO board);
   //읽어옴
   public BoardVO read(Long bno);
   //no를 참조해서 삭제하는데 bno를 쓰니까 long타입으로
   public int delete(Long bno);
   public int update(BoardVO board);
   
}