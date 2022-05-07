"""
On election day, 
a voting machine writes data in the form (voter_id, candidate_id) to a text file.
 Write a program that reads this file as a stream
  and returns the top 3 candidates at any given time.
   If you find a voter voting more than once, report this as fraud.
"""

def parse_line(line):
    line = line.strip()
    voter_id, candidate_id = line.split(',')
    return voter_id.strip(), candidate_id.strip()

def get_top_candidates(candidate_score_map):
    return list(zip(*sorted(candidate_score_map.items(), key=lambda item: item[1], reverse=True)))[0][:3]

if __name__ == "__main__":
    """
    1.read line by line
    """
    candidate_score_map = {}
    voter_list = []

    with open("./sample_data/problem_1114_voter_response.txt", "r") as rfile:
        for line in rfile.readlines():
            voter_id, candidate_id = parse_line(line)
            # raising fraud if duplicate voter id present
            if voter_id in voter_list:
                raise Exception(f"Fraud detected, voter duplicated : {voter_id}")
            voter_list.append(voter_id)
            if candidate_id not in candidate_score_map:
                candidate_score_map[candidate_id] = 0
            candidate_score_map[candidate_id] += 1
            top_candidates = get_top_candidates(candidate_score_map)
            print(f'[main] The top 3 candidates are :: {top_candidates}')
    print({c: candidate_score_map[c] for c in top_candidates})           
            
            