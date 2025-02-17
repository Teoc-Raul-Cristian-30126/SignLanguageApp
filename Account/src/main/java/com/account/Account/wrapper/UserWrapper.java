package com.account.Account.wrapper;

import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
public class UserWrapper {
    private Integer id;
    private String fistName;
    private String lastName;
    private String email;
    private String password;

    public UserWrapper(Integer id, String fistName, String lastName, String email, String password) {
        this.id = id;
        this.fistName = fistName;
        this.lastName = lastName;
        this.email = email;
        this.password = password;
    }

    public UserWrapper(String fistName, String lastName) {
        this.fistName = fistName;
        this.lastName = lastName;
    }
}
