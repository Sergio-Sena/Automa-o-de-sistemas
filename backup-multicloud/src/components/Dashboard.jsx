import React from 'react'
import { motion } from 'framer-motion'
import { Cloud, HardDrive, Clock, CheckCircle } from 'lucide-react'

const Dashboard = () => {
  const cloudProviders = [
    {
      name: 'AWS S3',
      status: 'connected',
      usage: '15.2 GB',
      color: 'from-orange-500 to-yellow-500',
      icon: '☁️'
    },
    {
      name: 'Google Cloud',
      status: 'connected',
      usage: '8.7 GB',
      color: 'from-blue-500 to-cyan-500',
      icon: '☁️'
    }
  ]

  const recentBackups = [
    { name: 'MySQL Database', time: '2 horas atrás', status: 'success', size: '2.1 GB' },
    { name: 'Documents Folder', time: '1 dia atrás', status: 'success', size: '856 MB' },
    { name: 'PostgreSQL DB', time: '2 dias atrás', status: 'success', size: '1.4 GB' },
  ]

  return (
    <div className="space-y-6">
      {/* Cloud Status Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {cloudProviders.map((provider, index) => (
          <motion.div
            key={provider.name}
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: index * 0.1 }}
            className="glass-card p-6"
          >
            <div className="flex items-center justify-between mb-4">
              <div className="flex items-center space-x-3">
                <div className={`w-12 h-12 rounded-xl bg-gradient-to-r ${provider.color} flex items-center justify-center text-2xl`}>
                  {provider.icon}
                </div>
                <div>
                  <h3 className="font-semibold text-lg">{provider.name}</h3>
                  <div className="flex items-center space-x-2">
                    <div className="w-2 h-2 bg-green-500 rounded-full"></div>
                    <span className="text-sm text-green-400">Conectado</span>
                  </div>
                </div>
              </div>
              <div className="text-right">
                <p className="text-2xl font-bold text-neon-cyan">{provider.usage}</p>
                <p className="text-sm text-gray-400">Usado</p>
              </div>
            </div>
            <div className="w-full bg-gray-700 rounded-full h-2">
              <div className={`h-2 rounded-full bg-gradient-to-r ${provider.color}`} style={{ width: '60%' }}></div>
            </div>
          </motion.div>
        ))}
      </div>

      {/* Stats Overview */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2 }}
          className="glass-card p-6 text-center"
        >
          <HardDrive className="w-8 h-8 text-neon-purple mx-auto mb-2" />
          <p className="text-2xl font-bold">23.9 GB</p>
          <p className="text-sm text-gray-400">Total Backup</p>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.3 }}
          className="glass-card p-6 text-center"
        >
          <Clock className="w-8 h-8 text-neon-cyan mx-auto mb-2" />
          <p className="text-2xl font-bold">22:00</p>
          <p className="text-sm text-gray-400">Próximo Backup</p>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.4 }}
          className="glass-card p-6 text-center"
        >
          <CheckCircle className="w-8 h-8 text-green-500 mx-auto mb-2" />
          <p className="text-2xl font-bold">98.5%</p>
          <p className="text-sm text-gray-400">Taxa de Sucesso</p>
        </motion.div>
      </div>

      {/* Recent Backups */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.5 }}
        className="glass-card p-6"
      >
        <h3 className="text-xl font-semibold mb-4 flex items-center">
          <Clock className="w-5 h-5 mr-2 text-neon-cyan" />
          Backups Recentes
        </h3>
        <div className="space-y-3">
          {recentBackups.map((backup, index) => (
            <div key={index} className="flex items-center justify-between p-3 bg-white/5 rounded-lg">
              <div className="flex items-center space-x-3">
                <CheckCircle className="w-5 h-5 text-green-500" />
                <div>
                  <p className="font-medium">{backup.name}</p>
                  <p className="text-sm text-gray-400">{backup.time}</p>
                </div>
              </div>
              <div className="text-right">
                <p className="font-medium text-neon-cyan">{backup.size}</p>
                <p className="text-sm text-green-400">Sucesso</p>
              </div>
            </div>
          ))}
        </div>
      </motion.div>
    </div>
  )
}

export default Dashboard