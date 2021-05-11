package org.conan.mapper;

import java.util.List;

/*import org.apache.ibatis.annotations.Select;*/
import org.conan.domain.BoardVO;

public interface BoardMapper {
   /* @Select("select * from tbl_board where bno>0") */
   //������� ������
   public List<BoardVO> getList();
   //������ PK���� �� �ʿ䰡 ���� ���
   public void insert(BoardVO board);
   //������ PK���� �˾ƾ��ϴ� ���
   public void insertSelectKey(BoardVO board);
   //�о��
   public BoardVO read(Long bno);
   //no�� �����ؼ� �����ϴµ� bno�� ���ϱ� longŸ������
   public int delete(Long bno);
   public int update(BoardVO board);
   
}