package jpabook.jpashop.domain;

import javax.persistence.*;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

@Entity
@Table(name="orders")
public class Order {
    @Id @GeneratedValue
    @Column(name="order_id")
    private Long id;

    //다대일 관계
    @ManyToOne
    @JoinColumn(name = "member_id")
    private Member member;

    private List<OrderItem> orderItems = new ArrayList<>();

    private Delivery delivery;
    
    private LocalDateTime orderDate; //주문시간

    private OrderStatus status; //주문상태(Order, Cancel)
}
