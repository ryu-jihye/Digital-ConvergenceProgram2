package org.conan.domain;

import org.springframework.stereotype.Component;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NonNull;
import lombok.ToString;
import lombok.Data;

@Data
public class SampleDTO {
	private String name;
	private int age;

}