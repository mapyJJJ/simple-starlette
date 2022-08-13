request = function()
    user_id = math.random(1, 10)
    path="/user/info?user_id=" .. user_id
    return wrk.format(nil, path)
end
