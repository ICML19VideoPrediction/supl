example = """    <tr>
  <td align="center" valign="middle"><a href="./Stochastic Video Prediction via Object-level Factorization/gym_gif/{:s}.gif"><img src="./Stochastic Video Prediction via Object-level Factorization/gym_gif/{:s}.gif" width="500"> </a></td>      
  <td align="center" valign="middle"><a href="./Stochastic Video Prediction via Object-level Factorization/gym_gif/{:s}.gif"><img src="./Stochastic Video Prediction via Object-level Factorization/gym_gif/{:s}.gif" width="500"> </a></td>
  </tr>
  """

list_file = 'demo_list.txt'

with open(list_file) as fp:
    vid_list = [line.strip() for line in fp]

wr_fp = open('tmp.html', 'w')
for i in range(0, len(vid_list), 2):
    if i == len(vid_list) - 1:
        to_str = example.format(vid_list[i], vid_list[i], vid_list[i], vid_list[i])
    else:
        to_str = example.format(vid_list[i], vid_list[i], vid_list[i + 1], vid_list[i + 1])
    wr_fp.write('%s' % to_str)
wr_fp.close()
