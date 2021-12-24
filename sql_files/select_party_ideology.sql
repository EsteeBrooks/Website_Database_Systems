select party.name party_name, ideology_name
from party natural inner join party_ideology natural inner join ideology;