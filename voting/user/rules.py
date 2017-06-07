import rules


@rules.predicate
def create_election(user):
    return user.role in [2, 3]

rules.add_rule('can_create_election', create_election)
