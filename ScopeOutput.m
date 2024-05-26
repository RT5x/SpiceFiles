close all;
clear;
format short;
format compact;


Scopefig = figure;
t = linspace(0, 10E-3);                                 % Time Vector (0 - 10ms)
f = 500;                                           % Desired Frequency (Cycles/Timespan)
sqwv = @(x) (5*sign(sin(2*pi*x*f)));     

for i = 1:numel(t)
     
    V(i) = (-1/((100000)*(0.05E-6)))*integral(sqwv,0,t(i));
    
end

plot(V,'LineWidth',0.5);
hold on

plot(sqwv(t));
axis([0 10 -8 8])
xlabel('t (ms)')

legend('Calculated Output Singal (V)', 'Theoretical Input signal (5 Vpp Square)','Location','northeast')
ylabel('V (V)')
box on
grid on
hold off
 

 savefig(Scopefig, 'Scopefig.fig');
print(Scopefig, '-dpng', 'Scopefig.png');