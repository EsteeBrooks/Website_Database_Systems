select party_id, name, seats, position_description
from party, position
where party.position_id = position.position_id;