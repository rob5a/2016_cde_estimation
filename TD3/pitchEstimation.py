# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 14:52:12 2015

Pitch estimation from gyro and accelero measurements
usign Kalman FIlter (small angles assumption)

@author: S. Bertrand
"""


import math
import KalmanFilter as kf
import numpy as np
import matplotlib.pyplot as plt
import ImuData as imud



if __name__=='__main__':

    # sampling period (s)
    '''
    # !!!!!!!!!!! A COMPLETER EN TD !!!!!!!!!!!!!!!!
    Te = 
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    '''
    
    
    # read data file
    fileName = 'donneesIMUPetitsAngles.txt'
    delimiter = '\t'
    imuMes = imud.ImuData(fileName, delimiter, Te)


    # system definition
    # state : pitch angle (rad), gyro's bias (rad/s)
    # input: pitch rate (rad/s) from gyro measurement
    # measurement : pitch angle (rad) computed from accelero measurements
        
    '''
    # !!!!!!!!!!! A COMPLETER EN TD !!!!!!!!!!!!!!!!
    nx = 
    nu = 
    ny =   
    Ak = 
    Bk = 
    Ck = 
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    '''
    
    # noises standrd deviation
    gyroPitchRateStdDev = 0.0065*0.0065  # (rad/s)
    gyroPitchRateBiasStdDev = 0.00005  # (rad/s)
    acceleroPitchStdDev = 0.01  # (rad)
    # covariance matrices
    Qk = Te * np.array( [ [math.pow(gyroPitchRateStdDev,2), 0.0], [0.0, math.pow(gyroPitchRateBiasStdDev,2)] ] )
    Rk = np.array([math.pow(acceleroPitchStdDev,2)])


    # initial state and covariance
    x0hat = np.array([ [0.0],[-0.006] ])
    P0 = np.array( [ [0.5,0.0],[0.0,0.1] ] )  
    
    
    # Kalman filter instantiation
    pitchKF = kf.KalmanFilter(nx, nu, ny)
    pitchKF.setStateEquation(Ak, Bk)
    pitchKF.setCk(Ck)
    pitchKF.setQk(Qk)
    pitchKF.setRk(Rk)
    pitchKF.initFilter( x0hat , P0 )
    


    # init data structures for simulation
    estimatedPitch = []
    estimatedPitch.append(x0hat[0,0])
    estimatedBias = []
    estimatedBias.append(x0hat[1,0])
    indicesK = [0]
    pitchImu = []


    # simulation loop
    for i in range(0, len(imuMes.time)):

        '''
        # !!!!!!!!!!! A COMPLETER EN TD !!!!!!!!!!!!!!!!
        # read pitch rate measurement i from gyro         
        uk = 

        # prediction step for Kalman filter with input uk
        pitchKF. _ _ _

        
        # compute pitch angle from accelero measurements i
        yk = 
    
        # update step for Kalman filter with measurement yk
        pitchKF.update(yk)

        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        '''

        # add estimated pitch and bias to data to be plotted
        estimatedPitch.append( pitchKF.xk[0,0])
        estimatedBias.append(pitchKF.xk[1,0])
        indicesK.append(i+1)       
        # add reference pitch value computed by IMU to data to be plotted
        pitchImu.append( math.radians(  imuMes.pitchDeg[i] ) )
        
    
    # end of simulation loop ----------------------------------------
    
    
    # plot estimated pitch and reference value from IMU
    plt.figure()
    plt.plot(indicesK, estimatedPitch, color='r')
    plt.plot(indicesK[1:len(indicesK)], pitchImu, color='b')
    plt.set_ylabel('From KF (rad)')
    plt.set_xlabel('iteration')
    plt.grid(True)    
    
    # plot estimated gyro bias
    plt.figure()
    plt.plot(indicesK, estimatedBias, color = 'r')
    plt.grid(True)
    plt.set_ylabel('gyro bias estimate (rad/s)')
    plt.set_xlabel('iteration')