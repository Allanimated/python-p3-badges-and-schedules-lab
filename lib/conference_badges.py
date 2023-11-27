def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badge_messages_list = [f"Hello, my name is {name}." for name in names]
    return badge_messages_list

def assign_rooms(names):
    new_list = [f"Hello, {name}! You'll be assigned to room {names.index(name) + 1}!" for name in names]
    return new_list

def printer(names):
    batch_badge_creator_list = batch_badge_creator(names)
    assign_rooms_list = assign_rooms(names)
    message_list = [*batch_badge_creator_list, *assign_rooms_list]
    for message in message_list:
        print(message)
