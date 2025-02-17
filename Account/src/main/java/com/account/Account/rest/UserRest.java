package com.account.Account.rest;

import com.account.Account.wrapper.UserWrapper;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@CrossOrigin(origins = "*")
@RequestMapping(path = "/user")
public interface UserRest {
    @PostMapping(path = "/addUser")
    ResponseEntity<String> addUser(@RequestBody(required = true) Map<String, String> requestMap);

    @GetMapping(path = "/login")
    ResponseEntity<UserWrapper> login(@RequestBody(required = true) Map<String, String> requestMap);
}
