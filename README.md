React Native - https://youtu.be/0-S5a0eXPoc
React Typescript - https://youtu.be/NjN00cM18Z4


# Creating a react native app with typescript
    - Command: npx react-native init ChuckNoris --template react-native-template-typescript

# Running React native app in android:
    - npx react-native run-android

# Testing your endpoints
    - Adding a Todo: curl --header "Content-Type: application/json" --request POST --data "{\"id\":\"1\",\"Title\":\"My Todo\",\"Description\":\"My Description\"}" http://<Your wifi ipv4 address>:3000/addTodo
    - Deleting a Todo: curl --header "Content-Type: application/json" --request DELETE http://<Your wifi ipv4 address>:3000/deleteTodo?id=<value>
    - Retrieving Todos: curl http://<Your wifi ipv4 address>:3000/getTodos
    - Retrieving Random Joke: curl http://<Your wifi ipv4 address>:3000/randomJoke
