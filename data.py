def getData():
    
    train_data = [
            (
                'update email of account coke to ab@gmail.com',
                [(len('update email of account '), len('update email of account coke'), 'ACC'),(len('update email of account abc to '), len('update email of account abc to ab@gmail.com'), 'EMAIL')]
            ),
            (
                'want to update email of account coke to ab@gmail.com',
                [(len('want to update email of account '), len('want to update email of account coke'), 'ACC'),(len('want to update email of account coke to '), len('want to update email of account coke to ab@gmail.com'), 'EMAIL')]         
            ),
            (
                'want to update id of account coke to ab@gmail.com',
                [(len('want to update id of account '), len('want to update id of account coke'), 'ACC'),(len('want to update id of account coke to '), len('want to update id of account coke to ab@gmail.com'), 'EMAIL')]         
            ),
            (
                'want to update email id of account coke to ab@gmail.com',
                [(len('want to update email id of account '), len('want to update email id of account coke'), 'ACC'),(len('want to update email id of account coke to '), len('want to update email id of account coke to ab@gmail.com'), 'EMAIL')]         
            ),
            (
                'get my email updated for coke to gf@gmail.com',
                [(len('get my email updated for '), len('get my email updated for coke'), 'ACC'),(len('get my email updated for coke to '), len('get my email updated for coke to gf@gmail.com'), 'EMAIL')]         
            ),
            (
                'wanna get my email updated for coke to gf@gmail.com',
                [(len('wanna get my email updated for '), len('wanna get my email updated for coke'), 'ACC'),(len('wanna get my email updated for coke to '), len('wanna get my email updated for coke to gf@gmail.com'), 'EMAIL')]         
            ),
            (
                'wanna get my email id updated for coke to gf@gmail.com',
                [(len('wanna get my email id updated for '), len('wanna get my email id updated for coke'), 'ACC'),(len('wanna get my email id updated for coke to '), len('wanna get my email id updated for coke to gf@gmail.com'), 'EMAIL')]         
            ),
            (
                'get my email id updated for coke to gf@gmail.com',
                [(len('get my email id updated for '), len('get my email id updated for coke'), 'ACC'),(len('get my email id updated for coke to '), len('get my email id updated for coke to gf@gmail.com'), 'EMAIL')]         
            ),
            (
                'I want to get my email updated for coke to gf@gmail.com',
                [(len('I want to get my email updated for '), len('I want to get my email updated for coke'), 'ACC'),(len('I want to get my email updated for coke to '), len('I want to get my email updated for coke to gf@gmail.com'), 'EMAIL')]         
            ),
            (
                'I want to get my email id updated for coke to gf@gmail.com',
                [(len('I want to get my email id updated for '), len('I want to get my email id updated for coke'), 'ACC'),(len('I want to get my email id updated for coke to '), len('I want to get my email id updated for coke to gf@gmail.com'), 'EMAIL')]         
            ),
            (
                'Please get my email updated for coke to gf@gmail.com',
                [(len('Please get my email updated for '), len('Please get my email updated for coke'), 'ACC'),(len('Please get my email updated for coke to '), len('Please get my email updated for coke to gf@gmail.com'), 'EMAIL')]         
            ),
            (
                'Please get my email id updated for coke to gf@gmail.com',
                [(len('Please get my email id updated for '), len('Please get my email id updated for coke'), 'ACC'),(len('Please get my email id updated for coke to '), len('Please get my email id updated for coke to gf@gmail.com'), 'EMAIL')]         
            ),
            (
                'I wish to update my email for coke to ab@gmail.com',
                [(len('I wish to update my email for '), len('I wish to update my email for coke'), 'ACC'),(len('I wish to update my email for coke to '), len('I wish to update my email for coke to ab@gmail.com'), 'EMAIL')]         
            ),
            (
                'I wish to update my email id for coke to ab@gmail.com',
                [(len('I wish to update my email id for '), len('I wish to update my email id for coke'), 'ACC'),(len('I wish to update my email id for coke to '), len('I wish to update my email id for coke to ab@gmail.com'), 'EMAIL')]         
            ),
            (
                'get my email id updated for account coke to ab@gmail.com',
                [(len('get my email id updated for account '), len('get my email id updated for account coke'), 'ACC'),(len('get my email id updated for account for coke to '), len('get my email id updated for account coke to ab@gmail.com'), 'EMAIL')]         
            ),
            (
                'get my email updated for account coke to ab@gmail.com',
                [(len('get my email updated for account '), len('get my email updated for account coke'), 'ACC'),(len('get my email updated for account for coke to '), len('get my email updated for account coke to ab@gmail.com'), 'EMAIL')]         
            ),
            (
                'update email of account abc to ab@gmail.com',
                [(len('update email of account '), len('update email of account abc'), 'ACC'),(len('update email of account abc to '), len('update email of account abc to ab@gmail.com'), 'EMAIL')]
            ),
            (
                'need to update my email id shubam@outlook.com for peps',
                [(len('need to update my email id shubam@outlook.com for '), len('need to update my email id shubam@outlook.com for peps'), 'ACC'),(len('need to update my email id '), len('need to update my email id shubam@outlook.com'), 'EMAIL')]
            ),
            (
                'change my email id to sh@cognizant.com for peps account',
                [(len('change my email id to sh@cognizant.com for '), len('change my email id to sh@cognizant.com for peps'), 'ACC'),(len('change my email id to '), len('change my email id to sh@cognizant.com'), 'EMAIL')]
            ),
            (
                'account name is peps and new email id is abc@gmail.com, kindly make the change',
                [(len('account name is '), len('account name is peps'), 'ACC'),(len('account name is peps and new email id is '), len('account name is peps and new email id is abc@gmail.com'), 'EMAIL')]
            ),
            (
                'Change the email for peps account to xyz@cognizant.com',
                [(len('Change the email for '), len('Change the email for peps'), 'ACC'),(len('Change the email for peps account to '), len('Change the email for peps account to xyz@cognizant.com'), 'EMAIL')]
            ),
            (
                'update my new email id shubam@cognizant.com for peps account',
                [(len('update my new email id shubam@cognizant.com for '), len('update my new email id shubam@cognizant.com for peps'), 'ACC'),(len('update my new email id '), len('pdate my new email id shubam@cognizant.com'), 'EMAIL')]
            ),
            (
                'make the change in peps for new email abc@outlook.com',
                [(len('make the change in '), len('make the change in peps'), 'ACC'),(len('make the change in peps for new email '), len('make the change in peps for new email abc@outlook.com'), 'EMAIL')]
            ),
            (
                'transmute my mail id to sh@cognizant.com for peps account',
                [(len('transmute my mail id to sh@cognizant.com for '), len('transmute my mail id to sh@cognizant.com for peps'), 'ACC'),(len('transmute my mail id to '), len('transmute my mail id to sh@cognizant.com'), 'EMAIL')]
            ),
            (
                'change my email to sh@cognizant.com in peps account',
                [(len('change my email to sh@cognizant.com in '), len('change my email to sh@cognizant.com in peps'), 'ACC'),(len('change my email to '), len('change my email to sh@cognizant.com'), 'EMAIL')]
            ),
            (
                'Email change request to sha@gmail.com for peps',
                [(len('Email change request to sha@gmail.com for '), len('Email change request to sha@gmail.com for peps'), 'ACC'),(len('Email change request to '), len('Email change request to sha@gmail.com'), 'EMAIL')]
            ),
            (
                'raise a request to change my email for peps to shubam@cognizant.com',
                [(len('raise a request to change my email for '), len('raise a request to change my email for peps'), 'ACC'),(len('raise a request to change my email for peps to '), len('raise a request to change my email for peps to shubam@cognizant.com'), 'EMAIL')]
            ),
            (
                'make a change request for email id for peps account to shubam@gmail.com',
                [(len('make a change request for email id for '), len('make a change request for email id for peps'), 'ACC'),(len('make a change request for email id for peps account to '), len('make a change request for email id for peps account to shubam@gmail.com'), 'EMAIL')]
            ),
            (
                'Can you update my mailing address to abc@cognizant.com for peps',
                [(len('Can you update my mailing address to abc@cognizant.com for '), len('Can you update my mailing address to abc@cognizant.com for peps'), 'ACC'),(len('Can you update my mailing address to '), len('Can you update my mailing address to abc@cognizant.com'), 'EMAIL')]
            ),
            (
                'plz update my email address to babc@gmail.com for account name abc',
                [(len('plz update my email address to babc@gmail.com for account name '), len('plz update my email address to babc@gmail.com for account name abc'), 'ACC'),(len('plz update my email address to '), len('plz update my email address to babc@gmail.com'), 'EMAIL')]
            ),
            (
                'update abc account email address to babc@gmail.com',
                [(len('update '), len('update abc'), 'ACC'),(len('update abc account email address to '), len('update abc account email address to  babc@gmail.com'), 'EMAIL')]
            ),
            (
                'update email address of hal account',
                [(len('update email address of '), len('update email address of hal'), 'ACC')]
            ),
            (
                'update email address of google',
                [(len('update email address of '), len('update email address of google'), 'ACC')]
            ),
            (
                'update email address of google account',
                [(len('update email address of '), len('update email address of google'), 'ACC')]
            ),
            (
                'update email of google',
                [(len('update email of '), len('update email of google'), 'ACC')]
            ),
            (
                'update email to ab@gmail.com of google account',
                [(len('update email address of '), len('update email address of google'), 'ACC'),(len('update email to '), len('update email to ab@gmail.com'), 'EMAIL')]
            ),
        ]
    return train_data