package com.account.Account.service;

import com.account.Account.wrapper.UserWrapper;
import org.springframework.http.ResponseEntity;

import java.util.Map;

public interface UserService {
    ResponseEntity<String> addUser(Map<String, String> requestMap);

    ResponseEntity<UserWrapper> login(Map<String, String> requestMap);
}
