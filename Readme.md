# Blog API Backend

### Database Models and Schemas

#### User (Table)

1. id
2. name
3. email
4. password
5. contact_no/mobile_no
6. phoneNumber
7. gender
8. age
9. date of birth
10. profile_pic
11. description (bio)
12. role (default = User)

#### Post

1. id
2. title
3. subtitle
4. description
5. created_at
6. updated_at

#### Post Media

1. id
2. media image/video/gif
3. uploaded_by

#### Comment

1. id
2. name
3. user_id (commented_by)
4. post_id

#### Categories

1. id
2. name
3. slug

#### Reaction

1. id
2. user_id
3. post_id
4. reaction

#### Shared_Post

1. id
2. user_post_id (This is the post id which is being shared)
3. user_id
4. post_id (This is the new created post which means the comment on the shared post)

#### Content_Visibility

1. id
2. name (Public,Private)

#### Notifications

1. id
2. user_id
3. category / type
4. message
5. is_read

#### Followers

1. id
2. follower_user_id
3. following_user_id

#### Workspace / ChatSpace

1. id
2. created_by
3. title
4. description
5. visibility

#### Education

#### Address

### Relation of Tables

1. One User can Post Many posts but One post cannot be done my many users

