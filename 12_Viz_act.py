from Utils import *
lower = -1
upper = 1
step = .1

data = pd.read_csv('data_full.csv')
data_fid = pd.read_csv('fid_full.csv')


fig = plt.figure()

'''Tanh'''
label = 'tanh'
# Creating the figure with four subplots, 2 per column/row
y = (data.y_tanh*2)-1
x = data.x
y_quantum = (data.tanh_quantum*2)+1
y_classic = (data.tanh_classical*2)+1


ax = plt.subplot(221)
ax.plot(x, y, label=label)
ax.plot(x, y_quantum, color='red', linestyle='dotted')
ax.plot(x, y_classic, color='limegreen', linestyle='dashed')
x_fid = data_fid.x
ax.scatter(x_fid, data_fid.tanh, color = 'cyan', label = 'Fidelity', s = 10)
ax.set_xlim(-1.1, 1.1)
#ax.set_ylim(-.1,1.1)
#ax.grid(True, which='minor', alpha = 0.3)
#ax.set_xlabel(r'x')
ax.set_title(label)



''' Sigmoid '''
label = 'sigmoid'


# Creating the figure with four subplots, 2 per column/row
y = data.y_sig
x = data.x

ax3 = plt.subplot(222)
ax3.plot(x, y, label=label)
ax3.plot(x, data.sig_quantum, color='red', linestyle='dotted')
ax3.plot(x, data.sig_classical, color='limegreen', linestyle='dashed')
ax3.scatter(x_fid, data_fid.sig, color = 'cyan', label = 'Fidelity', s = 10)
ax3.set_xlim(-1.1, 1.1)
#ax.set_ylim(-.1,1.1)
#ax.grid(True, which='minor', alpha = 0.3)
#ax.set_xlabel(r'x')
ax3.set_title(label)
ax3.set_xticks(np.round(np.arange(-1, 1.1, .4),1).tolist())




'''Relu'''
label = 'relu'

# Creating the figure with four subplots, 2 per column/row
y = data.y_relu-1

ax1 = plt.subplot(224)
ax1.plot(x, y, label=label)
ax1.plot(x, data.relu_quantum, color='red', linestyle='dotted')
ax1.plot(x, data.relu_classical, color='limegreen', linestyle='dashed')
x_fid = data_fid.x
ax1.scatter(x_fid, data_fid.tanh, color = 'cyan', label = 'Fidelity', s = 10)
ax1.set_xlim(-1.1, 1.1)
#ax.set_ylim(-.1,1.1)
ax1.grid( alpha = 0.3)
#ax.set_xlabel(r'x')
ax1.set_title(label)
ax1.set_xticks(np.round(np.arange(-1, 1.1, .2),1).tolist())



''' Elu '''
label = 'elu'

# Creating the figure with four subplots, 2 per column/row
y = data.y_elu-0.3
x = data.x
y_quantum = data.elu_quantum +0.7
y_classic = data.elu_classical+0.7

ax2 = plt.subplot(223)
ax2.plot(x, y, label=label)
ax2.plot(x, y_quantum, color='red', linestyle='dotted')
ax2.plot(x, y_classic, color='limegreen', linestyle='dashed')
x_fid = data_fid.x
ax2.scatter(x_fid, data_fid.elu, color = 'cyan', label = 'Fidelity', s = 10)
ax2.set_xlim(-1.1, 1.1)
#ax.set_ylim(-.1,1.1)
#ax.grid(True, which='minor', alpha = 0.3)
#ax.set_xlabel(r'x')
ax2.set_title(label)

handles, labels = ax.get_legend_handles_labels()
fig.legend(handles, labels, loc='lower center', bbox_to_anchor=(0.5, -0.5),
           ncol = 4, borderaxespad=1 )

#fig.savefig(folder + 'results_4x.png', bbox_extra_artists=(leg, suptitle,), bbox_inches='tight')
plt.show()
plt.close()


#
# functions = ['sigmoid', 'elu', 'arctan', 'relu', 'tanh']
# data = pd.read_csv(folder + f + '_data.csv')
#
# for f in functions:
#     data = pd.read_csv(folder + f + '_data.csv')
#     data_fid = pd.read_csv(folder + f + '_fidelity.csv')
#     data_fid.x = np.arange(lower + .05, upper, step).tolist()
#     data_fid.columns = ['fidelity', 'x']




# x = data_full.x
# functions = ['relu', 'elu', 'tanh', 'sig']
#
# fig=plt.figure()
# ax1 = plt.subplot(221)
# ax2 = plt.subplot(222)
# ax3 = plt.subplot(223)
# ax4 = plt.subplot(224)
#
# f = functions[0]
# y = data_full['y_'+f]
# # ax1.plot(x, y)
# # ax.plot(xs, cs(xs), label = 'Cubic Spline')
# qy = data_full[f+'_quantum']
# cy = data_full[f + '_classical']
# ax1.plot(x, qy, color='red', linestyle='dotted')
# ax1.plot(x, cy, color='green', linestyle='dashed')
# x_fid = fid_full.x
# fid = fid_full[f]
# ax1.scatter(x_fid, fid, color = 'limegreen', label = 'Fidelity', s = 7)
# ax1.set_xlim(-1.1, 1.1)
# ax1.set_ylim(-.1,1.1)
# ax1.grid(which = 'both', alpha = 0.3)
# # ax.set_xlabel(r'x')
# # ax1.set_ylabel(r'$f(x)$')
# ax1.text(0.80, 0.1, 'Relu',
#         transform=ax1.transAxes, ha="left")
#
#
#
# f = functions[1]
# # y = data_full['y_'+f]
# # ax2.plot(x, y)
# # ax.plot(xs, cs(xs), label = 'Cubic Spline')
# qy = data_full[f+'_quantum']
# cy = data_full[f + '_classical']
# ax2.plot(x, qy, color='red', linestyle='dotted')
# ax2.plot(x, cy, color='green', linestyle='dashed')
# x_fid = fid_full.x
# fid = fid_full[f]
# ax2.scatter(x_fid, fid, color = 'limegreen', label = 'Fidelity', s = 7)
# ax2.set_xlim(-1, 1.1)
# ax2.set_ylim(-.6,1.1)
# ax2.grid(alpha = 0.3)
# # ax.set_xlabel(r'x')
# # ax1.set_ylabel(r'$f(x)$')
# ax2.text(0.8, .1, 'Elu',
#         transform=ax2.transAxes, ha="left")
#
#
#
# f = functions[2]
# #y = data_full['y_'+f]
# #ax3.plot(x, y)
# # ax.plot(xs, cs(xs), label = 'Cubic Spline')
# qy = data_full[f+'_quantum']
# cy = data_full[f + '_classical']
# ax3.plot(x, qy, color='red', linestyle='dotted')
# ax3.plot(x, cy, color='green', linestyle='dashed')
# x_fid = fid_full.x
# fid = fid_full[f]
# ax3.scatter(x_fid, fid, color = 'limegreen', label = 'Fidelity', s = 7)
# ax3.set_xlim(-1.1, 1.1)
# #ax3.set_ylim(-.1,1.1)
# ax3.grid(alpha = 0.3)
# # ax.set_xlabel(r'x')
# # ax1.set_ylabel(r'$f(x)$')
# ax3.text(0.6, 0.1, 'Hyperbolic Tangent',
#         transform=ax3.transAxes, ha="center")
#
#
#
# f = functions[3]
# #y = data_full['y_'+f]
# #ax4.plot(x, y)
# # ax.plot(xs, cs(xs), label = 'Cubic Spline')
# qy = data_full[f+'_quantum']
# cy = data_full[f + '_classical']
# ax4.plot(x, qy, color='red', linestyle='dotted', label = 'Quantum Spline')
# ax4.plot(x, cy, color='green', linestyle='dashed', label = 'Classical Spline')
# x_fid = fid_full.x
# fid = fid_full[f]
# ax4.scatter(x_fid, fid, color = 'limegreen', label = 'Fidelity', s = 7)
# ax4.set_xlim(-1.1, 1.1)
# ax4.set_ylim(-.1,1.1)
# ax4.grid(which = 'major', alpha = 0.3)
# # ax.set_xlabel(r'x')
# # ax1.set_ylabel(r'$f(x)$')
# ax4.text(.65, .1, 'Sigmoid',
#         transform=ax4.transAxes, ha="left")
# # plt.legend()
# plt.savefig('results/full_spline.png', dpi =1000)
#
# # Creating legend and title for the figure. Legend created with figlegend(), title with suptitle()
# handles, labels = ax4.get_legend_handles_labels()
# fig.legend(handles, labels, loc='lower center', bbox_to_anchor=(0.5, 0.),
#            ncol = 3, borderaxespad=0)

# # plt.legend()
# plt.savefig('results/full_spline.png', dpi =800)
# plt.show()
# plt.close()
#
# rss_quantum = [np.sum(np.square(data_full.y_relu - data_full.relu_quantum)),
#                np.sum(np.square(data_full.y_elu - data_full.elu_quantum)),
#                np.sum(np.square(data_full.y_tanh - data_full.tanh_quantum)),
#                np.sum(np.square(data_full.y_sig - data_full.sig_quantum)),
#                np.sum(np.square(data_full.y_arct - data_full.arct_quantum))]
#
# rss_classical = [np.sum(np.square(data_full.y_relu - data_full.relu_classical)),
#                np.sum(np.square(data_full.y_elu - data_full.elu_classical)),
#                np.sum(np.square(data_full.y_tanh - data_full.tanh_classical)),
#                np.sum(np.square(data_full.y_sig - data_full.sig_classical)),
#                  np.sum(np.square(data_full.y_arct - data_full.arct_classical))]
#
# fid_avg = [ np.average(fid_full.relu), np.average(fid_full.elu), np.average(fid_full.tanh),
#             np.average(fid_full.sig), np.average(fid_full.arct)]
#
#
# tab = pd.DataFrame([pd.Series(functions + ['arct']), pd.Series(rss_classical),
#                    pd.Series(rss_quantum), pd.Series(fid_avg)])
#
# tab = tab.transpose()
# tab.columns = ['Function', 'RSS (classical)', 'RSS(Quantum)', 'AVG FIdelity']
#
# tab.to_csv('results/table_results.csv', index = False)
