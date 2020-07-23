- ~~react to post interactor~~
    - ~~react to post given invalid post id raises exception~~
    - ~~react to post given dup reaction  results undo reaction~~
    - ~~react to post given diff reaction results update reaction~~
    
- ~~delete post interactor~~
    - ~~given invalid post id raise exception~~
    - ~~given invalid user_id raise exception~~
    - ~~given valid post deletes posts~~
 
- ~~react to comment interactor~~
    - ~~given invalid comment_id raise exception~~
    - ~~given valid comment_id, if reaction does't not exist then create reaction.~~
    - ~~given valid comment_id, if reaction exists and duplicate reaction occurs then undo reaction~~
    - ~~given valid comment_id, if reaction exists and different reaction occurs then update reaction~~
    
- ~~reply_to_comment_interactor~~
    - ~~with invalid comment_id raise exception.~~
    - ~~with valid comment_id, if it is really comment then reply~~
    - ~with valid comment_id, if it is not comment then reply to the parent_comment_id.~~

- ~~get posts with more positive reactions~~
    - ~~get posts with more positive reactions~~

- ~~get_reactions_to_post~~
    - ~~with invalid post_id raise exception~~
    - ~~with valid post_id return post reactions~~
    
- **get reaction metrics of a post**
    - **with invalid post_id raise exception** 
    - with valid post_id get reaction metrics**

    
<Refactor Check List>
1) Clean code
2) **create_autospec **
3) optimal