select party.name, politician.name, seats
from party, politician
where party.party_leader = politician.politician_id;
