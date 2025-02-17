package com.account.Account.serviceImpl;

import com.account.Account.POJO.User;
import com.account.Account.constants.AccountConstants;
import com.account.Account.dao.UserDao;
import com.account.Account.service.UserService;
import com.account.Account.utils.AccountUtils;
import com.account.Account.wrapper.UserWrapper;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

import java.util.Map;
import java.util.Objects;
import java.util.Optional;

@RequiredArgsConstructor
@Service
public class UserServiceImpl implements UserService {
    private final UserDao userDao;

    @Override
    public ResponseEntity<String> addUser(Map<String, String> requestMap) {
        try {
            User user = userDao.findByEmail(requestMap.get("email"));
            if (Objects.isNull(user)){
                userDao.save(getUserFromMap(requestMap));
                return AccountUtils.getResponseEntity(AccountConstants.USER_ADDED_SUCCESSFULLY, HttpStatus.OK);
            } else {
                return AccountUtils.getResponseEntity(AccountConstants.EMAIL_EXISTS, HttpStatus.BAD_REQUEST);
            }
        } catch (Exception exception) {
            exception.printStackTrace();
        }

        return AccountUtils.getResponseEntity(AccountConstants.SOMETHING_WENT_WRONG, HttpStatus.INTERNAL_SERVER_ERROR);
    }

    @Override
    public ResponseEntity<UserWrapper> login(Map<String, String> requestMap) {
        try {
            Optional<UserWrapper> optional = Optional.ofNullable(userDao.getUserAccount(requestMap.get("email"), requestMap.get("password")));;
            if (!optional.isEmpty()) {
                return new ResponseEntity<>(userDao.getUserAccount(requestMap.get("email"), requestMap.get("password")), HttpStatus.OK);
            } else {
                return new ResponseEntity<>(new UserWrapper(), HttpStatus.BAD_REQUEST);
            }
        } catch (Exception exception) {
            exception.printStackTrace();
        }

        return new ResponseEntity<>(new UserWrapper(), HttpStatus.INTERNAL_SERVER_ERROR);
    }

    private User getUserFromMap(Map<String, String> requestMap) {
        User user = new User();
        user.setFirstName(requestMap.get("firstName"));
        user.setLastName(requestMap.get("lastName"));
        user.setEmail(requestMap.get("email"));
        user.setPassword(requestMap.get("password"));

        return user;
    }
}