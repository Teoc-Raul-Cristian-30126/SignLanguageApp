package com.account.Account.restImpl;

import com.account.Account.rest.UserRest;
import com.account.Account.service.UserService;
import com.account.Account.wrapper.UserWrapper;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;

@CrossOrigin(origins = "*")
@RequiredArgsConstructor
@RestController
public class UserRestImpl implements UserRest {
    private final UserService userService;
    @Override
    public ResponseEntity<String> addUser(Map<String, String> requestMap) {
        try {
            return userService.addUser(requestMap);
        } catch (Exception ex) {
            ex.printStackTrace();
        }
        return null;
    }

    @Override
    public ResponseEntity<UserWrapper> login(Map<String, String> requestMap) {
        try {
            return userService.login(requestMap);
        } catch (Exception ex) {
            ex.printStackTrace();
        }
        return null;
    }
}
