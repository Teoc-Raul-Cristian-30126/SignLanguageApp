package com.account.Account.dao;

import com.account.Account.POJO.User;
import com.account.Account.wrapper.UserWrapper;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.repository.query.Param;

public interface UserDao extends JpaRepository<User, Integer> {
    UserWrapper getUserAccount(@Param("email") String email, @Param("password") String password);
    User findByEmail(@Param("email") String email);
}
