import React, { useState } from 'react'
import { motion } from 'framer-motion'
import { Cloud, Database, Settings, Activity } from 'lucide-react'
import Dashboard from './components/Dashboard'
import BackupConfig from './components/BackupConfig'
import CloudSettings from './components/CloudSettings'
import Logs from './components/Logs'

function App() {
  const [activeTab, setActiveTab] = useState('dashboard')

  const tabs = [
    { id: 'dashboard', label: 'Dashboard', icon: Activity },
    { id: 'backup', label: 'Backup', icon: Database },
    { id: 'settings', label: 'Configurações', icon: Settings },
    { id: 'logs', label: 'Logs', icon: Cloud },
  ]

  const renderContent = () => {
    switch (activeTab) {
      case 'dashboard':
        return <Dashboard />
      case 'backup':
        return <BackupConfig />
      case 'settings':
        return <CloudSettings />
      case 'logs':
        return <Logs />
      default:
        return <Dashboard />
    }
  }

  return (
    <div className="min-h-screen bg-dark-bg">
      {/* Header */}
      <header className="glass-card m-4 p-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <Cloud className="w-8 h-8 text-neon-cyan" />
            <h1 className="text-2xl font-bold bg-gradient-to-r from-neon-cyan to-neon-purple bg-clip-text text-transparent">
              Backup Multi-Cloud
            </h1>
          </div>
          <div className="flex items-center space-x-2">
            <div className="w-3 h-3 bg-green-500 rounded-full animate-pulse"></div>
            <span className="text-sm text-gray-300">Online</span>
          </div>
        </div>
      </header>

      {/* Navigation */}
      <nav className="mx-4 mb-4">
        <div className="glass-card p-2">
          <div className="flex space-x-1">
            {tabs.map((tab) => {
              const Icon = tab.icon
              return (
                <motion.button
                  key={tab.id}
                  onClick={() => setActiveTab(tab.id)}
                  className={`flex items-center space-x-2 px-4 py-2 rounded-lg transition-all duration-300 ${
                    activeTab === tab.id
                      ? 'bg-neon-cyan/20 text-neon-cyan border border-neon-cyan/30'
                      : 'text-gray-400 hover:text-white hover:bg-white/10'
                  }`}
                  whileHover={{ scale: 1.05 }}
                  whileTap={{ scale: 0.95 }}
                >
                  <Icon className="w-4 h-4" />
                  <span className="text-sm font-medium">{tab.label}</span>
                </motion.button>
              )
            })}
          </div>
        </div>
      </nav>

      {/* Content */}
      <main className="mx-4 pb-4">
        <motion.div
          key={activeTab}
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.3 }}
        >
          {renderContent()}
        </motion.div>
      </main>
    </div>
  )
}

export default App