import React, { useState } from 'react';
import styled from 'styled-components';

// Styled Components
const DashboardContainer = styled.div`
  display: flex;
  height: 100vh;
  background-color: #f4f4f4;
  overflow-x: hidden; /* Prevent horizontal scroll */
`;

const Sidebar = styled.div`
  width: 250px;
  background-color: #145a32;
  color: white;
  display: flex;
  flex-direction: column;
  padding: 20px;
  transition: all 0.3s ease;
  overflow-y: auto;
  height: 100vh;
  justify-content: flex-start; /* Ensure it aligns to top of the sidebar */

  &:hover {
    background-color: #1f8341;
  }
`;

const SidebarItem = styled.div`
  padding: 15px 10px;
  margin: 5px 0;
  cursor: pointer;
  border-radius: 5px;
  transition: background-color 0.3s ease, transform 0.2s ease;
  display: flex;
  align-items: center;

  &:hover {
    background-color: #27ae60;
    transform: scale(1.05);
  }

  &.active {
    background-color: #2ecc71;
  }

  svg {
    margin-right: 10px;
  }
`;

const Topbar = styled.div`
  width: 100%;
  height: 60px;
  background-color: white;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  display: flex;
  align-items: center;
  justify-content: flex-start; /* Align elements to the left */
  padding: 0 20px;
`;

const Content = styled.div`
  flex: 1;
  padding: 20px;
  overflow-y: auto;
  max-width: 100%;
  box-sizing: border-box;
`;

const DashboardTitle = styled.h1`
  color: #145a32;
  font-family: 'Courier New', Courier, monospace;
`;

const NotificationBell = styled.div`
  cursor: pointer;
  font-size: 1.5rem;
  color: #145a32;
  position: relative;
  margin-top: 20px; /* Add margin to space it out from the top items */

  &:hover {
    color: #27ae60;
  }

  span {
    position: absolute;
    top: -5px;
    right: -10px;
    background-color: red;
    color: white;
    border-radius: 50%;
    padding: 5px 8px;
    font-size: 0.9rem;
  }
`;

const FormGroup = styled.div`
  margin-bottom: 20px;
`;

const Input = styled.input`
  padding: 10px;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
  width: 100%;
  transition: border-color 0.3s ease;

  &:focus {
    border-color: #27ae60;
  }
`;

const Textarea = styled.textarea`
  padding: 10px;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
  width: 100%;
  height: 150px;
  transition: border-color 0.3s ease;

  &:focus {
    border-color: #27ae60;
  }
`;

const Icon = styled.i`
  font-size: 1.2rem;
  margin-right: 8px;
`;

// New Styled Components for Profile Picture and Settings
const ProfilePicContainer = styled.div`
  margin-bottom: 20px;
`;

const ProfilePicLabel = styled.label`
  display: block;
  margin-bottom: 10px;
  font-weight: bold;
`;

const ProfilePicInput = styled.input`
  display: none;
`;

const ProfilePicButton = styled.label`
  cursor: pointer;
  background-color: #27ae60;
  color: white;
  padding: 10px 20px;
  border-radius: 5px;
  display: inline-block;

  &:hover {
    background-color: #2ecc71;
  }
`;

const Switch = styled.div`
  display: flex;
  align-items: center;
  justify-content: space-between;

  input[type='checkbox'] {
    transform: scale(1.5);
  }
`;

const Button = styled.button`
  padding: 10px 20px;
  background-color: #27ae60;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 20px;

  &:hover {
    background-color: #2ecc71;
  }
`;

const GroupContainer = styled.div`
  margin-bottom: 20px;
`;

const GroupList = styled.div`
  list-style-type: none;
  padding: 0;
`;

const GroupItem = styled.div`
  background-color: #e9f7ef;
  border-radius: 5px;
  margin: 10px 0;
  padding: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;

  &:hover {
    background-color: #d5f5e3;
  }
`;

// Resources Page Components
const ResourceContainer = styled.div`
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
`;

const ResourceItem = styled.div`
  background-color: #fff;
  border-radius: 5px;
  padding: 15px;
  width: 45%;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
`;

const ResourceTitle = styled.h3`
  color: #145a32;
`;

const ResourceDescription = styled.p`
  color: #666;
`;

const ResourceLink = styled.a`
  display: inline-block;
  color: #27ae60;
  font-weight: bold;
  margin-top: 10px;

  &:hover {
    text-decoration: underline;
  }
`;

// Author Dashboard Component
const AuthorDashboard = () => {
  const [activeTab, setActiveTab] = useState('manuscripts');
  const [notifications, setNotifications] = useState(3);
  const [profilePic, setProfilePic] = useState(null);
  const [emailNotifications, setEmailNotifications] = useState(true);
  const [profileVisibility, setProfileVisibility] = useState(true);
  const [groups, setGroups] = useState([
    { id: 1, name: 'Writing Mastermind', description: 'A group for sharing writing tips and feedback.' },
    { id: 2, name: 'Beta Readers Unite', description: 'Join this group to collaborate with fellow beta readers.' },
  ]);
  const [newGroupName, setNewGroupName] = useState('');
  const [newGroupDescription, setNewGroupDescription] = useState('');
  const [settings, setSettings] = useState({
    emailNotifications: true,
    profileVisibility: true,
    contactEmail: '',
    contactPhone: '',
    changePassword: false,
  });

  // Handle profile picture upload
  const handleProfilePicChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setProfilePic(URL.createObjectURL(file));
    }
  };

  // Handle creating a new group
  const handleCreateGroup = () => {
    if (newGroupName && newGroupDescription) {
      const newGroup = {
        id: groups.length + 1,
        name: newGroupName,
        description: newGroupDescription,
      };
      setGroups([...groups, newGroup]);
      setNewGroupName('');
      setNewGroupDescription('');
    }
  };

  // Handle joining a group
  const handleJoinGroup = (groupId) => {
    alert(`Joined group with ID: ${groupId}`);
  };

  // Handle Sign Out
  const handleSignOut = () => {
    alert('You have been signed out.');
    localStorage.removeItem('user');
    window.location.href = '/'; // Redirect to homepage
  };

  // Handle Notification Click
  const handleNotificationClick = () => {
    alert(`You have ${notifications} new notifications`);
  };

  // Handle setting change
  const handleSettingChange = (e) => {
    setSettings({
      ...settings,
      [e.target.name]: e.target.checked,
    });
  };

  // Handle contact input change
  const handleContactChange = (e) => {
    setSettings({
      ...settings,
      [e.target.name]: e.target.value,
    });
  };

  // Render content based on active tab
  const renderContent = () => {
    switch (activeTab) {
      case 'manuscripts':
        return (
          <>
            <DashboardTitle>Manuscript Submission</DashboardTitle>
            <p>Here, authors can submit their manuscripts for review, track progress, and manage submissions.</p>
            <FormGroup>
              <label htmlFor="manuscript-upload">Upload Manuscript:</label>
              <Input type="file" id="manuscript-upload" />
            </FormGroup>
            <FormGroup>
              <label htmlFor="manuscript-title">Manuscript Title:</label>
              <Input type="text" id="manuscript-title" placeholder="Enter manuscript title" />
            </FormGroup>
            <Button onClick={() => alert('Manuscript submitted for review!')}>Submit Manuscript</Button>
          </>
        );
      case 'profile':
        return (
          <>
            <DashboardTitle>Profile Settings</DashboardTitle>
            <ProfilePicContainer>
              <ProfilePicLabel>Upload Profile Picture</ProfilePicLabel>
              <ProfilePicInput type="file" accept="image/*" onChange={handleProfilePicChange} />
              <ProfilePicButton htmlFor="profile-pic">Choose a File</ProfilePicButton>
              {profilePic && <img src={profilePic} alt="Profile Pic" style={{ marginTop: '10px', width: '100px' }} />}
            </ProfilePicContainer>
            <FormGroup>
              <label htmlFor="bio">Bio:</label>
              <Textarea id="bio" placeholder="Write a short bio here..." />
            </FormGroup>
            <FormGroup>
            <label htmlFor="phone-number">Phone Number:</label>
            <Input
            type="tel"
            id="phone-number"
            placeholder="Enter your phone number"
            name="contactPhone"
            value={settings.contactPhone}
            onChange={handleContactChange}
            />
            <Button onClick={() => alert('Profile updated!')}>Save Changes</Button>
            </FormGroup>
            </>          
        );
      case 'resources':
        return (
          <>
            <DashboardTitle>Resources</DashboardTitle>
            <ResourceContainer>
              <ResourceItem>
                <ResourceTitle>Writing Templates</ResourceTitle>
                <ResourceDescription>Download templates for various types of writing, including novel outlines, character development, and plot structure.</ResourceDescription>
                <ResourceLink href="#">Download Now</ResourceLink>
              </ResourceItem>
              <ResourceItem>
                <ResourceTitle>Writing Tools</ResourceTitle>
                <ResourceDescription>Explore a range of tools designed to help writers streamline their writing process and stay productive.</ResourceDescription>
                <ResourceLink href="#">Explore Tools</ResourceLink>
              </ResourceItem>
            </ResourceContainer>
          </>
        );
      case 'groups':
        return (
          <>
            <DashboardTitle>Community Groups</DashboardTitle>
            <GroupContainer>
              <h3>Join a Group</h3>
              <GroupList>
                {groups.map((group) => (
                  <GroupItem key={group.id}>
                    <div>
                      <strong>{group.name}</strong>
                      <p>{group.description}</p>
                    </div>
                    <Button onClick={() => handleJoinGroup(group.id)}>Join Group</Button>
                  </GroupItem>
                ))}
              </GroupList>

              {/* Create Group Section */}
              <h4>Create New Group</h4>
              <FormGroup>
                <Input
                  type="text"
                  placeholder="Group Name"
                  value={newGroupName}
                  onChange={(e) => setNewGroupName(e.target.value)}
                />
              </FormGroup>
              <FormGroup>
                <Textarea
                  placeholder="Group Description"
                  value={newGroupDescription}
                  onChange={(e) => setNewGroupDescription(e.target.value)}
                />
              </FormGroup>
              <Button onClick={handleCreateGroup}>Create Group</Button>
            </GroupContainer>
          </>
        );
        case 'settings':
          return (
            <>
              <DashboardTitle>Account Settings</DashboardTitle>
        
              {/* Email Notifications */}
              <FormGroup>
                <label htmlFor="email-notifications">
                  <Switch>
                    <input
                      type="checkbox"
                      name="emailNotifications"
                      checked={settings.emailNotifications}
                      onChange={handleSettingChange}
                    />
                    <span>Email Notifications</span>
                  </Switch>
                </label>
              </FormGroup>
        
              {/* Profile Visibility */}
              <FormGroup>
                <label htmlFor="profile-visibility">
                  <Switch>
                    <input
                      type="checkbox"
                      name="profileVisibility"
                      checked={settings.profileVisibility}
                      onChange={handleSettingChange}
                    />
                    <span>Profile Visibility</span>
                  </Switch>
                </label>
              </FormGroup>
        
              {/* Contact Email */}
              <FormGroup>
                <label htmlFor="contact-email">Contact Email:</label>
                <Input
                  type="email"
                  id="contact-email"
                  name="contactEmail"
                  value={settings.contactEmail}
                  onChange={handleContactChange}
                />
              </FormGroup>
        
              {/* Contact Phone */}
              <FormGroup>
                <label htmlFor="contact-phone">Contact Phone:</label>
                <Input
                  type="text"
                  id="contact-phone"
                  name="contactPhone"
                  value={settings.contactPhone}
                  onChange={handleContactChange}
                />
              </FormGroup>
        
              {/* Portfolio Link */}
              <FormGroup>
                <label htmlFor="portfolio-link">Portfolio Link:</label>
                <Input
                  type="url"
                  id="portfolio-link"
                  name="portfolioLink"
                  value={settings.portfolioLink}
                  onChange={handleContactChange}
                  placeholder="Enter your portfolio URL"
                />
              </FormGroup>
        
              {/* Feedback Preference */}
              <FormGroup>
                <label htmlFor="feedback-preference">Feedback Preference:</label>
                <select
                  id="feedback-preference"
                  name="feedbackPreference"
                  value={settings.feedbackPreference}
                  onChange={handleSettingChange}
                >
                  <option value="email">Email</option>
                  <option value="platform">Platform</option>
                </select>
              </FormGroup>
        
              {/* Project Budget */}
              <FormGroup>
                <label htmlFor="budget-preference">Project Budget:</label>
                <Input
                  type="number"
                  id="budget-preference"
                  name="budgetPreference"
                  value={settings.budgetPreference}
                  onChange={handleContactChange}
                  placeholder="Enter your preferred project budget"
                />
              </FormGroup>
        
              {/* Allow Beta Readers */}
              <FormGroup>
                <label htmlFor="allow-beta-readers">
                  <Switch>
                    <input
                      type="checkbox"
                      name="allowBetaReaders"
                      checked={settings.allowBetaReaders}
                      onChange={handleSettingChange}
                    />
                    <span>Allow Beta Readers</span>
                  </Switch>
                </label>
              </FormGroup>
        
              {/* NDA Agreement for Manuscripts */}
              <FormGroup>
                <label htmlFor="nda-agreement">
                  <Switch>
                    <input
                      type="checkbox"
                      name="ndaAgreement"
                      checked={settings.ndaAgreement}
                      onChange={handleSettingChange}
                    />
                    <span>Require NDA for Manuscripts</span>
                  </Switch>
                </label>
                {settings.ndaAgreement && (
                  <>
                    {/* NDA Document Upload */}
                    <FormGroup>
                      <label htmlFor="nda-document">Upload NDA Document:</label>
                      <Input
                        type="file"
                        id="nda-document"
                        name="ndaDocument"
                        onChange={handleContactChange}
                      />
                    </FormGroup>
        
                    {/* NDA Status */}
                    <FormGroup>
                      <label htmlFor="nda-status">NDA Status:</label>
                      <p>{settings.ndaSigned ? 'NDA Signed by Beta Readers' : 'NDA Pending'}</p>
                    </FormGroup>
                  </>
                )}
              </FormGroup>
        
              {/* Social Links */}
              <FormGroup>
                <label htmlFor="social-link-facebook">Facebook:</label>
                <Input
                  type="url"
                  id="social-link-facebook"
                  name="facebookLink"
                  value={settings.facebookLink}
                  onChange={handleContactChange}
                  placeholder="Enter your Facebook URL"
                />
              </FormGroup>
              <FormGroup>
                <label htmlFor="social-link-twitter">Twitter:</label>
                <Input
                  type="url"
                  id="social-link-twitter"
                  name="twitterLink"
                  value={settings.twitterLink}
                  onChange={handleContactChange}
                  placeholder="Enter your Twitter URL"
                />
              </FormGroup>
              <FormGroup>
                <label htmlFor="social-link-linkedin">LinkedIn:</label>
                <Input
                  type="url"
                  id="social-link-linkedin"
                  name="linkedinLink"
                  value={settings.linkedinLink}
                  onChange={handleContactChange}
                  placeholder="Enter your LinkedIn URL"
                />
              </FormGroup>
        
              {/* Change Password Button */}
              <FormGroup>
                <Button onClick={() => alert('Password change functionality coming soon!')}>
                  Change Password
                </Button>
              </FormGroup>
        
              {/* Save Settings Button */}
              <Button onClick={() => alert('Settings saved!')}>Save Settings</Button>
            </>
          );
        
      default:
        return <p>Welcome to your dashboard!</p>;
    }
  };

  return (
    <DashboardContainer>
      <Sidebar>
      <NotificationBell
      onClick={handleNotificationClick}
      style={{ marginLeft: '150px' }} 
    >
      🔔 {notifications > 0 && `(${notifications})`}
    </NotificationBell>
        <SidebarItem
          className={activeTab === 'manuscripts' ? 'active' : ''}
          onClick={() => setActiveTab('manuscripts')}
        >
          <Icon className="fas fa-file-alt" /> Manuscripts
        </SidebarItem>
        <SidebarItem
          className={activeTab === 'profile' ? 'active' : ''}
          onClick={() => setActiveTab('profile')}
        >
          <Icon className="fas fa-user" /> Profile
        </SidebarItem>
        <SidebarItem
          className={activeTab === 'resources' ? 'active' : ''}
          onClick={() => setActiveTab('resources')}
        >
          <Icon className="fas fa-book" /> Resources
        </SidebarItem>
        <SidebarItem
          className={activeTab === 'groups' ? 'active' : ''}
          onClick={() => setActiveTab('groups')}
        >
          <Icon className="fas fa-users" /> Community Groups
        </SidebarItem>
        <SidebarItem
          className={activeTab === 'settings' ? 'active' : ''}
          onClick={() => setActiveTab('settings')}
        >
          <Icon className="fas fa-cogs" /> Settings
        </SidebarItem>
        <SidebarItem onClick={handleSignOut}>
          <Icon className="fas fa-sign-out-alt" /> Sign Out
        </SidebarItem>
      </Sidebar>

      <div style={{ flex: 1 }}>
  <Topbar style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
    <h2>Author Dashboard</h2>
  </Topbar>
  <Content>{renderContent()}</Content>
</div>

    </DashboardContainer>
  );
};

export default AuthorDashboard;
