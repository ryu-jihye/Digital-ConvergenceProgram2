package org.conan.domain;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

import org.springframework.format.annotation.DateTimeFormat;

import lombok.Data;


@Data
public class TodoDTO {//자주 쓰임
	private String title;
	@DateTimeFormat(pattern="yyyy/MM/dd")
	private Date dueDate;
	}

